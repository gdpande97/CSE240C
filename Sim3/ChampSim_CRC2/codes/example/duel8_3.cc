#include "../inc/champsim_crc2.h"
#include "../inc/BloomFilter.h"
#include <set>
#include <vector>
#include <array>
#include <cstdint>
#include <string>

using namespace std;

//Defining the global variables for both the policies.

#define maxRRPV 7
#define LLC_WAYS 16
#define NUM_CORE 1
#define MAX_LLC_SETS 8192

#define SAT_INC(x,max)  (x<max)?x+1:x
#define SAT_DEC(x)      (x>0)?x-1:x
#define TRUE 1
#define FALSE 0

#define RRIP_OVERRIDE_PERC   0

#define NUM_LEADER_SETS   64
#define maxSHCTR 7
#define SHCT_SIZE (1<<13)

//Load/Store instruction category
#define RANDOM 0
#define STREAMING 1
#define THRASH 2
#define FRIENDLY 3

#define SAMPLE_COUNT 100 // LLC_WAYS<<3 
#define OV_size 100


int LLC_SETS_LOG2 = 11;
int LLC_SETS ;
int ALIAS_TAB_SIZE = NUM_CORE * 64;


//data structures for the 2 policies

uint32_t rrpv[MAX_LLC_SETS][LLC_WAYS];    //rrpv table
vector<vector<uint32_t>> ov;      //occupancy vector
vector<vector<bool>> hv;          //hit vector
uint32_t id[8192];                //id is incremented and decremented
vector<vector<pair<uint64_t, uint64_t>>> history; //stores the history for every Belady trainer

set<int> sample_set;   //sampled set for belady trainer, count 20
BloomFilter* pc_friendly_filter;    //Friendly bin - KEEP
BloomFilter* pc_streaming_filter;   //Streaming bin - BYPASS
vector<pair<uint64_t,bool>> alias_table; //Random bin

set<int> lime_sample_set; //sampled set for LIME for dueling, count 64 as of now

//teh same rrpv table will be shared between the two
uint32_t is_prefetch[MAX_LLC_SETS][LLC_WAYS];  //is_prefetch is tracking if the line was prefetched
uint32_t fill_core[MAX_LLC_SETS][LLC_WAYS];  //fill core is used to fill for cpu

set<int> ship_sample_set;     //sample sets
uint32_t line_reuse[MAX_LLC_SETS][LLC_WAYS]; //??
uint64_t line_sig[MAX_LLC_SETS][LLC_WAYS];  //tracks signature of the line

uint32_t SHCT[NUM_CORE][SHCT_SIZE];   //Signature hit count table


//For statistics only
uint64_t insertion_distrib[NUM_TYPES][maxRRPV+1];
uint64_t total_prefetch_downgrades;


uint32_t select_counter;


//LIME Helper functions
uint32_t hash16(uint64_t pc)
{
    uint16_t pc0 = pc & 0x3fff;
    uint8_t bit32 = (pc & 0x100000000) >> 32;
    uint8_t bit40 = (pc & 0x10000000000) >> 40;
    uint16_t hash = pc0 + (bit40 <<16) + (bit32<<15) ;    
    return hash;
}

uint64_t hash30(uint64_t tag_addr)
{
    uint64_t top8 = (tag_addr<<(6+LLC_SETS_LOG2)) >> 56;
    uint64_t hash = (top8<<22) + (tag_addr&0x3fffff);
    return hash;
}

int getPCCategory(uint64_t pc)
{
    uint32_t target = hash16(pc); //hash1 return 16 bit
    bool friendly = pc_friendly_filter -> possiblyContains(target); 
    bool streaming = pc_streaming_filter -> possiblyContains(target); 
    if(friendly && streaming){
        vector<pair<uint64_t,bool>>::iterator it;
        for(it=alias_table.begin(); it!=alias_table.end(); it++){
            if((*it).first == target){
                if((*it).second==true)
                    return FRIENDLY;
                else
                    return STREAMING;
            }
        }
        //put target into alias_table
        if(alias_table.size()>ALIAS_TAB_SIZE){
            alias_table.erase(alias_table.begin());
        }
        pair<uint64_t,bool> alias_pc(target,true);
        alias_table.push_back(alias_pc);
        return FRIENDLY;
    }
        //return THRASH;
    else if (friendly)
        return FRIENDLY;
    else if (streaming)
        return STREAMING;
    else 
        return RANDOM;
}

void updatePCCategory(uint32_t pc, int new_cate)
{
    if (new_cate == FRIENDLY)
        pc_friendly_filter -> add(pc);
    else if (new_cate == STREAMING)
        pc_streaming_filter -> add(pc);
   
    vector<pair<uint64_t,bool>>::iterator it; 
    for(it=alias_table.begin(); it!=alias_table.end(); it++){
        if((*it).first == pc){
            if (new_cate == FRIENDLY)
                (*it).second=true;
            if (new_cate == STREAMING)
                (*it).second=false;
        }
    }
    return;
}

void InitReplacementState() {
    int cfg = get_config_number();
    int LLC_SETS = (get_config_number() <= 2) ? 2048 : MAX_LLC_SETS;

    for(int i = 0; i < LLC_SETS; i++) {
        for(int j = 0; j < LLC_WAYS; j++) {
            rrpv[i][j] = maxRRPV;
        }
    }
    
    pc_friendly_filter = new BloomFilter(4096, 6);
    pc_streaming_filter = new BloomFilter(4096, 6);

    int sample_sets_num = 20 * NUM_CORE;
    int duel_sets_num = 64 * NUM_CORE;
//    if(cfg == 1 || cfg == 2) {
        
        //replace this to make sure we have a selection in every constituency
    //int random_number[20]={46, 102, 257, 406, 510, 630, 772, 880, 981, 1088, 1163, 1206, 1311, 1436, 1543, 1644, 1735, 1810, 1956, 2017};
    //for(int i=0; i<sample_sets_num; i++){
    //	sample_set.insert(random_number[i]); //this will change to some selected numbers instead of random to create constituencies
   // 	lime_sample_set.insert(random_number[i]);
    //}
        //int other_rand[44] = {}; //enter 44 random numbers here
        //for(int i = 0; i < duel_sets_num - sample_sets_num; i++) {
          //  lime_sample_set.insert(random_number[i]);
        //}

//    }
//

    int constituency = 0; 

    for(int i=0; i<duel_sets_num; i++){
        int lime_set_num = rand()%32;
        lime_sample_set.insert(constituency + lime_set_num);
        if(constituency%96 == 0  && sample_set.size() <=sample_sets_num) {
            sample_set.insert(constituency + lime_set_num);
        }
        int ship_set_num = rand()%32;
        while(ship_set_num == lime_set_num) {
            ship_set_num = rand()%32;
        }
        ship_sample_set.insert(constituency + ship_set_num);
        constituency+=32;
    }

    for (int i=0; i<LLC_SETS; i++) {
        std::vector<uint32_t> init;
        ov.push_back(init);
        std::vector<bool> init2;
        hv.push_back(init2);
    }

    for (int i=0; i<LLC_SETS; i++){
        std::vector<pair<uint64_t, uint64_t>> init;
        history.push_back(init);
    }

    for (int i=0; i<LLC_SETS; i++) {
        id[i] = 0;
    }

    for (int i = 0; i < MAX_LLC_SETS; i++) {
        for (int j = 0; j < LLC_WAYS; j++) {
            line_reuse[i][j] = FALSE;
            is_prefetch[i][j] = FALSE;
            line_sig[i][j] = 0;
        }
    }

    for (int i=0; i<NUM_CORE; i++) {
        for (int j=0; j<SHCT_SIZE; j++) {
            SHCT[i][j] = 1; // Assume weakly re-use start
        }
    }


 //   while(ship_sample_set.size() < NUM_LEADER_SETS) {
 //       int randval = rand()%LLC_SETS;
 //       if(lime_sample_set.find(randval) != lime_sample_set.end()) {
 //           continue;
 //       } else {
 //           ship_sample_set.insert(randval);
 //       }

 //   }


    select_counter = 511;
}

uint32_t GetVictimInSet (uint32_t cpu, uint32_t set, const BLOCK *current_set, uint64_t PC, uint64_t paddr, uint32_t type) {

    if(lime_sample_set.find(set) != lime_sample_set.end() || (!ship_sample_set.count(set) && select_counter >= 512)) {
        if(type == 3) //WRTIEBACK returns 0 always
            return 0;

        if(type == 2) //PREFETCH returns 16 - bypass always
            return LLC_WAYS;

        if(getPCCategory(PC) == STREAMING && type!=3){ 
            return LLC_WAYS;
        }


    }

    while (1) {
        for (int i=0; i<LLC_WAYS; i++)
            if (rrpv[set][i] == maxRRPV){ //rrpv is used by both SHIP++ and LIME
                return i;
            }
        for (int i=0; i<LLC_WAYS; i++)
            rrpv[set][i]++;
    }

    // WE SHOULD NOT REACH HERE
    assert(0);
    return 0;
}


void shipUpdateReplacementState (uint32_t cpu, uint32_t set, uint32_t way, uint64_t paddr, uint64_t PC, uint64_t victim_addr, uint32_t type, uint8_t hit) {
uint32_t sig   = line_sig[set][way];

    if (hit) { // update to REREF on hit
        if( type != WRITEBACK ) 
        {
            
            if( (type == PREFETCH) && is_prefetch[set][way] )
            {
//                line_rrpv[set][way] = 0;
                //check with monil if this is multicore config    
                if( (ship_sample_set.find(set) != ship_sample_set.end()) && ((rand()%100 <5) || (get_config_number()==4))) 
                {
                    uint32_t fill_cpu = fill_core[set][way];

                    SHCT[fill_cpu][sig] = SAT_INC(SHCT[fill_cpu][sig], maxSHCTR);
                    line_reuse[set][way] = TRUE;
                }
            }
            else 
            {
                rrpv[set][way] = 0;

                if( is_prefetch[set][way] )
                {
                    rrpv[set][way] = maxRRPV;
                    is_prefetch[set][way] = FALSE;
                    total_prefetch_downgrades++;
                }

                if( (ship_sample_set.find(set) != ship_sample_set.end()) && (line_reuse[set][way]==0) ) 
                {
                    uint32_t fill_cpu = fill_core[set][way];

                    SHCT[fill_cpu][sig] = SAT_INC(SHCT[fill_cpu][sig], maxSHCTR);
                    line_reuse[set][way] = TRUE;
                }
            }
        }
        
	return;
    }
    
    //--- All of the below is done only on misses -------
    // remember signature of what is being inserted
    uint64_t use_PC = (type == PREFETCH ) ? ((PC << 1) + 1) : (PC<<1);
    uint32_t new_sig = use_PC%SHCT_SIZE;
    //done only if its a sampled set -> check on how to incorporate sampled sets, or do we just use these sampled sets for dueling? i think the latter
    if(ship_sample_set.find(set) != ship_sample_set.end()) 
    {
        uint32_t fill_cpu = fill_core[set][way];
        
        // update signature based on what is getting evicted
        if (line_reuse[set][way] == FALSE) { 
            SHCT[fill_cpu][sig] = SAT_DEC(SHCT[fill_cpu][sig]);
        }
        else 
        {
            SHCT[fill_cpu][sig] = SAT_INC(SHCT[fill_cpu][sig], maxSHCTR);
        }

        line_reuse[set][way] = FALSE;
        line_sig[set][way]   = new_sig;  
        fill_core[set][way]  = cpu;
    }



    is_prefetch[set][way] = (type == PREFETCH);

    // Now determine the insertion prediciton

    uint32_t priority_RRPV = maxRRPV-1 ; // default SHIP

    if( type == WRITEBACK )
    {
        rrpv[set][way] = maxRRPV;
    }
    else if (SHCT[cpu][new_sig] == 0) {
        rrpv[set][way] = (rand()%100>=RRIP_OVERRIDE_PERC)?  maxRRPV: priority_RRPV; //LowPriorityInstallMostly
    }
    else if (SHCT[cpu][new_sig] == 7) {
        rrpv[set][way] = (type == PREFETCH) ? 1 : 0; // HighPriority Install
    }
    else {
        rrpv[set][way] = priority_RRPV; // HighPriority Install 
    }

    // Stat tracking for what insertion it was at
    insertion_distrib[type][rrpv[set][way]]++;

}

void limeUpdateReplacementState (uint32_t cpu, uint32_t set, uint32_t way, uint64_t paddr, uint64_t PC, uint64_t victim_addr, uint32_t type, uint8_t hit) {
      if(type==3 || type==2) // do not train on writeback or prefetch
        return; 

    //all changes below done only for belady trainers -if pc is one of the sampled sets
    if(sample_set.find(set) != sample_set.end()){
/*
        if(set == 46)
            cout << "cfg 1/2" << endl;
        if(set == 7494)
            cout << "cfg 3/4" << endl;
*/
        uint64_t tag_addr = paddr >> (6 + LLC_SETS_LOG2);
            // ---- Update History
        if (history[set].size() >= OV_size) {
            if(hv[set][0] == false){
                int new_cate = 1; //STREAMING
                uint64_t ori_pc = history[set][0].second;
                updatePCCategory(ori_pc, new_cate);
            }
            history[set].erase( history[set].begin());
            ov[set].erase(ov[set].begin());
            hv[set].erase(hv[set].begin());
            id[set] --;
        } 


        // ---- Update OV HV
        pair<uint64_t, uint64_t> paddr_PC (hash30(tag_addr), hash16(PC));
        history[set].push_back(paddr_PC);
        ov[set].push_back(0);
        hv[set].push_back(false);

        int end = id[set];
        int start = -1;
        for (int i = end-1; i >=0; i--){
            if (history[set][i].first == paddr_PC.first){
                start = i;
                break;
            }
        }
        id[set] ++;
        if (start >= 0){
            bool keep = true;
            for(int i=start; i<end; i++){
                keep = keep && (ov[set][i]<LLC_WAYS-1);
                if(!keep)
                    break;
            }
            uint64_t ori_pc = history[set][start].second;
            int new_cate;
            if(keep){
                hv[set][start] = true;
                for (int i=start; i < end; i++)
                    ov[set][i] += 1;
                new_cate = FRIENDLY; //FRIENDLY
                updatePCCategory(ori_pc, new_cate);
            }else{
                new_cate = STREAMING; //STREAMING
                updatePCCategory(ori_pc, new_cate);
            }
        }
    }
 //from here training done for all sets, not just sampled ones
    if(way == LLC_WAYS){
        return; 
    }
    int category = getPCCategory(PC);

    if(hit == 1){
        switch(category){
            case RANDOM:
                if(rrpv[set][way] >  (maxRRPV-4))
                    rrpv[set][way] = maxRRPV-4;
                break;
            case STREAMING:
                rrpv[set][way] = maxRRPV-4;
                break;
            case THRASH:
            case FRIENDLY:
                rrpv[set][way] = 0;
                break;
        }
    }
    else{
        switch(category){
            case RANDOM:
                rrpv[set][way] = maxRRPV-1;
                break;
            case STREAMING:
                rrpv[set][way] = maxRRPV-1;
                break;
            case THRASH:
            case FRIENDLY:
                rrpv[set][way] = 0;
                for(uint64_t i=0; i< LLC_WAYS; i++){
                    if(i != way && (rrpv[set][i] < 6))
                        rrpv[set][i]+=1;
                }
                break;
        }

    }
    return; 
}


void UpdateReplacementState (uint32_t cpu, uint32_t set, uint32_t way, uint64_t paddr, uint64_t PC, uint64_t victim_addr, uint32_t type, uint8_t hit) {
    uint8_t dir = 2;
    if(lime_sample_set.find(set) != lime_sample_set.end()) {
        if(hit == 0)
            dir = 1;
        limeUpdateReplacementState(cpu, set, way, paddr, PC, victim_addr, type, hit);
    } else if (ship_sample_set.find(set) != ship_sample_set.end()) {
        if(hit == 0)
            dir = 0;        
        shipUpdateReplacementState(cpu, set, way, paddr, PC, victim_addr, type, hit);
    } else if(select_counter >= 512) {
//        if(hit == 0)
//            dir = 1;
        limeUpdateReplacementState(cpu, set, way, paddr, PC, victim_addr, type, hit);
    } else {
//        if(hit == 0)
//            dir = 0;
        shipUpdateReplacementState(cpu, set, way, paddr, PC, victim_addr, type, hit);
    }
    if(dir == 1) {
        select_counter--;
    } else if(dir == 0) {
        select_counter++;
    }
    if(select_counter > 1023) {
        select_counter = 1023;
    }
    if(select_counter < 0) {
        select_counter = 0;
    }
}

void PrintStats_Heartbeat()
{
	cout << "select_counter is " << select_counter << endl;
}

string names[] = 
{
    "LOAD", "RFO", "PREF", "WRITEBACK" 
};


void PrintStats()
{

    set<int>:: iterator itr;
    cout<<"Ship samples: "<<endl;
    for(itr=ship_sample_set.begin(); itr != ship_sample_set.end(); itr++) {
	    cout<<*itr<< ", ";
    }
    cout<<endl;
    cout<<"Lime duel samples: "<<endl;
    for(itr=lime_sample_set.begin(); itr != lime_sample_set.end(); itr++) {
	    cout<<*itr<< ", ";
    } 
    cout<<endl;
    cout<<"Lime samples: "<<endl;
    for(itr=sample_set.begin(); itr != sample_set.end(); itr++) {
	    cout<<*itr<<", ";
    }
    cout<<endl;
    cout<<"Insertion Distribution: "<<endl;
    for(uint32_t i=0; i<NUM_TYPES; i++) 
    {
        cout<<"\t"<<names[i]<<" ";
        for(uint32_t v=0; v<maxRRPV+1; v++) 
        {
            cout<<insertion_distrib[i][v]<<" ";
        }
        cout<<endl;
    }

    cout<<"Total Prefetch Downgrades: "<<total_prefetch_downgrades<<endl;

}

