////////////////////////////////////////////
//                                        //
//        LIME replacement policy         //
//                                        //
////////////////////////////////////////////

////////////////////////////////////////////
//                                        //
//     SRRIP [Jaleel et al. ISCA' 10]     //
//     Jinchun Kim, cienlux@tamu.edu      //
//                                        //
////////////////////////////////////////////

#include "../inc/champsim_crc2.h"
#include "BloomFilter.h"
#include <set>
#include <vector>
#include <array>
#include <cstdint>
#include <string>

using namespace std;

/******************LIME*******************/

int NUM_CORE; 
int LLC_SETS ;
int LLC_SETS_LOG2 ;
#define LLC_WAYS 16
#define maxRRPV 7

//Load/Store instruction category
#define RANDOM 0
#define STREAMING 1
#define THRASH 2
#define FRIENDLY 3

//
#define SAMPLE_COUNT 128 // LLC_WAYS<<3 
#define OV_size 128
int ALIAS_TAB_SIZE;

uint32_t rrpv[8192][LLC_WAYS];
uint64_t cold_misses;
vector<vector<uint32_t>> ov;
vector<vector<bool>> hv;
uint32_t id[8192];
vector<vector<pair<uint64_t, uint64_t>>> history;

BloomFilter** data_filter;
set<int> sample_set;
BloomFilter* pc_friendly_filter;
BloomFilter* pc_streaming_filter;
vector<pair<uint64_t,bool>> alias_table;

/******************SHIP++*******************/
#define NUM_CORE 1
#define MAX_LLC_SETS 8192
#define LLC_WAYS 16

#define SAT_INC(x,max)  (x<max)?x+1:x
#define SAT_DEC(x)      (x>0)?x-1:x
#define TRUE 1
#define FALSE 0

#define RRIP_OVERRIDE_PERC   0


// The base policy is SRRIP. SHIP needs the following on a per-line basis
#define maxRRPV 3
uint32_t line_rrpv[MAX_LLC_SETS][LLC_WAYS];
uint32_t is_prefetch[MAX_LLC_SETS][LLC_WAYS];
uint32_t fill_core[MAX_LLC_SETS][LLC_WAYS];

// These two are only for sampled sets (we use 64 sets)
#define NUM_LEADER_SETS   64

uint32_t ship_sample[MAX_LLC_SETS];
uint32_t line_reuse[MAX_LLC_SETS][LLC_WAYS];
uint64_t line_sig[MAX_LLC_SETS][LLC_WAYS];
	
// SHCT. Signature History Counter Table
// per-core 16K entry. 14-bit signature = 16k entry. 3-bit per entry
#define maxSHCTR 7
#define SHCT_SIZE (1<<14)
uint32_t SHCT[NUM_CORE][SHCT_SIZE];


// Statistics
uint64_t insertion_distrib[NUM_TYPES][maxRRPV+1];
uint64_t total_prefetch_downgrades;

//End data structures for SHIP++


/**************Data structures for dueling*******************/

uint32_t select_counter = 512;

vector<uint32_t> lime_sampled_set;
vector<uint32_t> ship_sampled_set;

// initialize replacement state


uint32_t hash18(uint64_t pc)
{
    uint16_t pc0 = pc & 0xffff;
    uint8_t bit32 = (pc & 0x100000000) >> 32;
    uint8_t bit40 = (pc & 0x10000000000) >> 40;
    uint16_t hash = pc0 + (bit40 <<18) + (bit32<<17) ;    
    return hash;
}

uint64_t hash37(uint64_t tag_addr)
{
    uint64_t top8 = (tag_addr<<(6+LLC_SETS_LOG2)) >> 56;
    uint64_t hash = (top8<<29) + (tag_addr&0x1fffffff);
    return hash;
}

int getPCCategory(uint64_t pc)
{
    uint32_t target = hash18(pc); //hash1 return 16 bit
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


void InitReplacementState()
{
    int cfg = get_config_number();

    for (int i=0; i<LLC_SETS; i++) {
        for (int j=0; j<LLC_WAYS; j++) {
            rrpv[i][j] = maxRRPV;
        }
    }
    
    pc_friendly_filter = new BloomFilter(4096, 6);
    pc_streaming_filter = new BloomFilter(4096, 6);


    int sample_sets_num = 20*NUM_CORE;
    if(cfg==1 || cfg == 2){
        int random_number[20]={46, 102, 257, 406, 510, 630, 772, 880, 981, 1088, 1163, 1206, 1311, 1436, 1543, 1644, 1735, 1810, 1956, 2017};
        for(int i=0; i<sample_sets_num; i++){
            sample_set.insert(random_number[i]); //this will change to some selected numbers instead of random to create constituencies
        }
    }
    else if(cfg==3 || cfg==4){
        int random_number[80]={187, 201, 286, 332, 449, 642, 675, 682, 744, 770, 883, 1013, 1085, 1227, 1237, 1298, 1310, 1333, 1358, 1671, 1728, 1812, 1819, 1963, 2295, 2410, 2450, 2508, 2553, 2592, 2700, 2976, 3084, 3359, 3557, 3780, 3879, 4303, 4328, 4397, 4428, 4514, 4561, 4852, 4897, 4943, 5000, 5187, 5314, 5361, 5532, 5535, 5635, 5646, 5718, 5853, 5898, 5917, 6056, 6164, 6340, 6435, 6827, 6839, 6852, 6944, 7174, 7466, 7494, 7496, 7497, 7519, 7524, 7604, 7638, 7788, 7830, 8152, 8158, 8173};
        for(int i=0; i<sample_sets_num; i++){
            sample_set.insert(random_number[i]);
        }
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


    /************************Finish LIME Start SHIP++************************/

    int LLC_SETS = (get_config_number() <= 2) ? 2048 : MAX_LLC_SETS;

    cout << "Initialize SRRIP state" << endl;

    for (int i=0; i<MAX_LLC_SETS; i++) {
        for (int j=0; j<LLC_WAYS; j++) {
            line_rrpv[i][j] = maxRRPV;
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

    int leaders=0;

    while(leaders<NUM_LEADER_SETS){
      int randval = rand()%LLC_SETS;  //this will change to some selected numbers instead of random to create constituencies
      
      if(ship_sample[randval]==0){
	ship_sample[randval]=1;
	leaders++;
      }
    }

/*************************Finish SHIP++************************/

}

// find replacement victim
// return value should be 0 ~ 15 or 16 (bypass)
uint32_t GetVictimInSet (uint32_t cpu, uint32_t set, const BLOCK *current_set, uint64_t PC, uint64_t paddr, uint32_t type)
{



    if(select_counter >=512 || lime_sampled_set.find(set) != lime_sampled_set.end()) {
        if(type == 3)
            return 0;

        if(type == 2)
            return LLC_WAYS;

        if(getPCCategory(PC) == STREAMING && type!=3){
            return LLC_WAYS;
        }
    }
    
 //below code is same for ship++ and lime, above needs an if condition which will select which policy.
    // look for the maxRRPV line
    while (1)
    {
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

//  /************************SHIP++**********************/

// // look for the maxRRPV line
//     while (1)
//     {
//         for (int i=0; i<LLC_WAYS; i++)
//             if (line_rrpv[set][i] == maxRRPV) { // found victim
//                 return i;
//             }

//         for (int i=0; i<LLC_WAYS; i++)
//             line_rrpv[set][i]++;
//     }

//     // WE SHOULD NOT REACH HERE
//     assert(0);
//     return 0;

}

// called on every cache hit and cache fill
void UpdateReplacementState (uint32_t cpu, uint32_t set, uint32_t way, uint64_t paddr, uint64_t PC, uint64_t victim_addr, uint32_t type, uint8_t hit)
{

    if(sample_set.find(set) !=sample_set.end()) {

    if(type==3 || type==2) // do not train on writeback or prefetch
        return; 
    if(sample_set.find(set) != sample_set.end()){

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
        pair<uint64_t, uint64_t> paddr_PC (hash37(tag_addr), hash18(PC));
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
    /*********************SHIP++ update**********************/


    uint32_t sig   = line_sig[set][way];

    if (hit) { // update to REREF on hit
        if( type != WRITEBACK ) 
        {

            if( (type == PREFETCH) && is_prefetch[set][way] )
            {
//                line_rrpv[set][way] = 0;
                
                if( (ship_sample[set] == 1) && ((rand()%100 <5) || (get_config_number()==4))) 
                {
                    uint32_t fill_cpu = fill_core[set][way];

                    SHCT[fill_cpu][sig] = SAT_INC(SHCT[fill_cpu][sig], maxSHCTR);
                    line_reuse[set][way] = TRUE;
                }
            }
            else 
            {
                line_rrpv[set][way] = 0;

                if( is_prefetch[set][way] )
                {
                    line_rrpv[set][way] = maxRRPV;
                    is_prefetch[set][way] = FALSE;
                    total_prefetch_downgrades++;
                }

                if( (ship_sample[set] == 1) && (line_reuse[set][way]==0) ) 
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
    
    if( ship_sample[set] == 1 ) 
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
        line_rrpv[set][way] = maxRRPV;
    }
    else if (SHCT[cpu][new_sig] == 0) {
      line_rrpv[set][way] = (rand()%100>=RRIP_OVERRIDE_PERC)?  maxRRPV: priority_RRPV; //LowPriorityInstallMostly
    }
    else if (SHCT[cpu][new_sig] == 7) {
        line_rrpv[set][way] = (type == PREFETCH) ? 1 : 0; // HighPriority Install
    }
    else {
        line_rrpv[set][way] = priority_RRPV; // HighPriority Install 
    }

    // Stat tracking for what insertion it was at
    insertion_distrib[type][line_rrpv[set][way]]++;

}

// use this function to print out your own stats on every heartbeat 
void PrintStats_Heartbeat()
{

}

string names[] = 
{
    "LOAD", "RFO", "PREF", "WRITEBACK" 
};


// use this function to print out your own stats at the end of simulation
void PrintStats()
{

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



//

// initialize replacement state
void InitReplacementState()
{
    
}

// find replacement victim
// return value should be 0 ~ 15 or 16 (bypass)
uint32_t GetVictimInSet (uint32_t cpu, uint32_t set, const BLOCK *current_set, uint64_t PC, uint64_t paddr, uint32_t type)
{
    
}

// called on every cache hit and cache fill
void UpdateReplacementState (uint32_t cpu, uint32_t set, uint32_t way, uint64_t paddr, uint64_t PC, uint64_t victim_addr, uint32_t type, uint8_t hit)
{
  

}


