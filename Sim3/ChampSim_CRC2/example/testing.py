Last login: Mon Feb 28 18:36:26 on ttys002
(base) gandhardeshpande@Gandhars-MacBook-Pro ~ % cat /dev/serial0
cat: /dev/serial0: No such file or directory
(base) gandhardeshpande@Gandhars-MacBook-Pro ~ % cd /dev
(base) gandhardeshpande@Gandhars-MacBook-Pro /dev % ls
aes_0				ptyw4
afsc_type5			ptyw5
apfs-raw-device.2.0		ptyw6
auditpipe			ptyw7
auditsessions			ptyw8
autofs				ptyw9
autofs_control			ptywa
autofs_homedirmounter		ptywb
autofs_notrigger		ptywc
autofs_nowait			ptywd
bpf0				ptywe
bpf1				ptywf
bpf2				random
bpf3				rdisk0
bpf4				rdisk0s1
console				rdisk0s2
cu.Bluetooth-Incoming-Port	rdisk0s3
cu.wlan-debug			rdisk1
disk0				rdisk1s1
disk0s1				rdisk1s2
disk0s2				rdisk1s3
disk0s3				rdisk1s4
disk1				rdisk2
disk1s1				rdisk2s1
disk1s2				rdisk2s2
disk1s3				rdisk3
disk1s4				rdisk3s1
disk2				rdisk3s1s1
disk2s1				rdisk3s2
disk2s2				rdisk3s3
disk3				rdisk3s4
disk3s1				rdisk3s5
disk3s1s1			rdisk3s6
disk3s2				stderr
disk3s3				stdin
disk3s4				stdout
disk3s5				tty
disk3s6				tty.Bluetooth-Incoming-Port
dtrace				tty.wlan-debug
dtracehelper			ttyp0
fbt				ttyp1
fd				ttyp2
fsevents			ttyp3
io8log				ttyp4
io8logmt			ttyp5
io8logtemp			ttyp6
klog				ttyp7
lockstat			ttyp8
monotonic			ttyp9
null				ttypa
oslog				ttypb
oslog_stream			ttypc
perfmon_core			ttypd
perfmon_uncore			ttype
pf				ttypf
pfm				ttyq0
profile				ttyq1
ptmx				ttyq2
ptyp0				ttyq3
ptyp1				ttyq4
ptyp2				ttyq5
ptyp3				ttyq6
ptyp4				ttyq7
ptyp5				ttyq8
ptyp6				ttyq9
ptyp7				ttyqa
ptyp8				ttyqb
ptyp9				ttyqc
ptypa				ttyqd
ptypb				ttyqe
ptypc				ttyqf
ptypd				ttyr0
ptype				ttyr1
ptypf				ttyr2
ptyq0				ttyr3
ptyq1				ttyr4
ptyq2				ttyr5
ptyq3				ttyr6
ptyq4				ttyr7
ptyq5				ttyr8
ptyq6				ttyr9
ptyq7				ttyra
ptyq8				ttyrb
ptyq9				ttyrc
ptyqa				ttyrd
ptyqb				ttyre
ptyqc				ttyrf
ptyqd				ttys0
ptyqe				ttys000
ptyqf				ttys001
ptyr0				ttys002
ptyr1				ttys1
ptyr2				ttys2
ptyr3				ttys3
ptyr4				ttys4
ptyr5				ttys5
ptyr6				ttys6
ptyr7				ttys7
ptyr8				ttys8
ptyr9				ttys9
ptyra				ttysa
ptyrb				ttysb
ptyrc				ttysc
ptyrd				ttysd
ptyre				ttyse
ptyrf				ttysf
ptys0				ttyt0
ptys1				ttyt1
ptys2				ttyt2
ptys3				ttyt3
ptys4				ttyt4
ptys5				ttyt5
ptys6				ttyt6
ptys7				ttyt7
ptys8				ttyt8
ptys9				ttyt9
ptysa				ttyta
ptysb				ttytb
ptysc				ttytc
ptysd				ttytd
ptyse				ttyte
ptysf				ttytf
ptyt0				ttyu0
ptyt1				ttyu1
ptyt2				ttyu2
ptyt3				ttyu3
ptyt4				ttyu4
ptyt5				ttyu5
ptyt6				ttyu6
ptyt7				ttyu7
ptyt8				ttyu8
ptyt9				ttyu9
ptyta				ttyua
ptytb				ttyub
ptytc				ttyuc
ptytd				ttyud
ptyte				ttyue
ptytf				ttyuf
ptyu0				ttyv0
ptyu1				ttyv1
ptyu2				ttyv2
ptyu3				ttyv3
ptyu4				ttyv4
ptyu5				ttyv5
ptyu6				ttyv6
ptyu7				ttyv7
ptyu8				ttyv8
ptyu9				ttyv9
ptyua				ttyva
ptyub				ttyvb
ptyuc				ttyvc
ptyud				ttyvd
ptyue				ttyve
ptyuf				ttyvf
ptyv0				ttyw0
ptyv1				ttyw1
ptyv2				ttyw2
ptyv3				ttyw3
ptyv4				ttyw4
ptyv5				ttyw5
ptyv6				ttyw6
ptyv7				ttyw7
ptyv8				ttyw8
ptyv9				ttyw9
ptyva				ttywa
ptyvb				ttywb
ptyvc				ttywc
ptyvd				ttywd
ptyve				ttywe
ptyvf				ttywf
ptyw0				uart.wlan-debug
ptyw1				urandom
ptyw2				zero
ptyw3
(base) gandhardeshpande@Gandhars-MacBook-Pro /dev % cat ttys0
^C
(base) gandhardeshpande@Gandhars-MacBook-Pro /dev % sudo cat ttys0
Password:
^C
(base) gandhardeshpande@Gandhars-MacBook-Pro /dev % cd 
(base) gandhardeshpande@Gandhars-MacBook-Pro ~ % ssh gdeshpande@dsmlp-login.ucsd.edu
(gdeshpande@dsmlp-login.ucsd.edu) Password: 
Last login: Mon Feb 28 09:11:44 2022 from rrcs-24-43-123-72.west.biz.rr.com
 

To see all available software packages, type "prep -l" at the command prompt,
or "prep -h" for more options.
quota: No filesystem specified.
Hello gdeshpande, you are currently logged into dsmlp-login.ucsd.edu

You are using 0% CPU on this system

[gdeshpande@dsmlp-login]:~:499$ kubectl get pods
NAME               READY   STATUS             RESTARTS   AGE
gdeshpande-29756   0/1     DeadlineExceeded   0          13h
[gdeshpande@dsmlp-login]:~:500$ kubectl delete pod gdeshpande-29756
pod "gdeshpande-29756" deleted
[gdeshpande@dsmlp-login]:~:501$ ls
ChampSim  ChampSim_CRC2  ipc1_public  run-docker.sh
[gdeshpande@dsmlp-login]:~:502$ cd ChampSim_CRC2/
[gdeshpande@dsmlp-login]:ChampSim_CRC2:503$ ls
CHANGELOG.txt    README.txt      benchmarks_all.txt  compile_all.sh      err.out  inc  lime_trial_result.txt  red_test  results  run_lime_base.sh        ship_trial_result.txt  trace     wakeup.sh
DESCRIPTION.txt  benchmarks.txt  bin                 compile_example.sh  example  lib  nohup.out              redo.sh   run.sh   ship4_trial_result.txt  test.sh                trial.sh
[gdeshpande@dsmlp-login]:ChampSim_CRC2:504$ rm nohup.out 
[gdeshpande@dsmlp-login]:ChampSim_CRC2:505$ l
-bash: l: command not found
[gdeshpande@dsmlp-login]:ChampSim_CRC2:506$ ls
CHANGELOG.txt    README.txt      benchmarks_all.txt  compile_all.sh      err.out  inc  lime_trial_result.txt  redo.sh  run.sh            ship4_trial_result.txt  test.sh  trial.sh
DESCRIPTION.txt  benchmarks.txt  bin                 compile_example.sh  example  lib  red_test               results  run_lime_base.sh  ship_trial_result.txt   trace    wakeup.sh
[gdeshpande@dsmlp-login]:ChampSim_CRC2:507$ vi compile_all.sh 
[gdeshpande@dsmlp-login]:ChampSim_CRC2:508$ vi compile_example.sh 
[gdeshpande@dsmlp-login]:ChampSim_CRC2:509$ vi red_test 
[gdeshpande@dsmlp-login]:ChampSim_CRC2:510$ vi redo.sh 
[gdeshpande@dsmlp-login]:ChampSim_CRC2:511$ cd example/
[gdeshpande@dsmlp-login]:example:512$ ls
Block.cc     dancrc2.cc  hawkeye_final.cc  lime.cc          lime_rrpv.cc  lime_tag_hash.cc  lru-8MB.cc  red.cc     ship_dse.cc   ship_trial.cc  srrip.cc
TagEntry.cc  ehc         leeway.cc         lime_pc_hash.cc  lime_size.cc  lime_trial.cc     lru.cc      ship++.cc  ship_size.cc  srrip-8MB.cc   tag.cc
[gdeshpande@dsmlp-login]:example:513$ vi duel.cc
[gdeshpande@dsmlp-login]:example:514$ cd ..
[gdeshpande@dsmlp-login]:ChampSim_CRC2:515$ g++ -Wall --std=c++11 -o bin/duel_first example/duel.cc lib/config2.a
-bash: g++: command not found
[gdeshpande@dsmlp-login]:ChampSim_CRC2:516$ launch-scipy-ml.sh -i zymajasper/cs240cwi22:v1 -c 8 -m 64 -b
Mon Feb 28 21:40:44 PST 2022 Submitting job gdeshpande-18822
pod/gdeshpande-18822 created
Mon Feb 28 21:40:45 PST 2022 INFO starting up - pod status: Pending ; Successfully assigned gdeshpande/gdeshpande-18822 to its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:40:48 PST 2022 INFO starting up - pod status: Pending ; Successfully assigned gdeshpande/gdeshpande-18822 to its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:40:50 PST 2022 INFO starting up - pod status: Pending ; Successfully assigned gdeshpande/gdeshpande-18822 to its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:40:52 PST 2022 INFO starting up - pod status: Pending ; Successfully assigned gdeshpande/gdeshpande-18822 to its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:40:54 PST 2022 INFO starting up - pod status: Pending ; Successfully assigned gdeshpande/gdeshpande-18822 to its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:40:57 PST 2022 INFO starting up - pod status: Pending ; Successfully assigned gdeshpande/gdeshpande-18822 to its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:40:59 PST 2022 INFO starting up - pod status: Pending ; Successfully assigned gdeshpande/gdeshpande-18822 to its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:41:01 PST 2022 INFO starting up - pod status: Pending ; Successfully assigned gdeshpande/gdeshpande-18822 to its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:41:04 PST 2022 INFO starting up - pod status: Pending ; Successfully assigned gdeshpande/gdeshpande-18822 to its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:41:06 PST 2022 INFO starting up - pod status: Pending ; Successfully assigned gdeshpande/gdeshpande-18822 to its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:41:08 PST 2022 INFO starting up - pod status: Pending ; Successfully assigned gdeshpande/gdeshpande-18822 to its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:41:10 PST 2022 INFO starting up - pod status: Pending ; Started container c1
Mon Feb 28 21:41:13 PST 2022 INFO pod assigned to node: its-dsmlp-n28.ucsd.edu
Mon Feb 28 21:41:13 PST 2022 INFO zymajasper/cs240cwi22:v1 is now active.
Connect to your background pod via: "kubesh gdeshpande-18822"
Please remember to shut down via: "kubectl delete pod gdeshpande-18822" ; "kubectl get pods" to list running pods.
You may retrieve output from your pod via: "kubectl logs gdeshpande-18822".
PODNAME=gdeshpande-18822
[gdeshpande@dsmlp-login]:ChampSim_CRC2:517$ kubesh gdeshpande-18822
gdeshpande@gdeshpande-18822:~$ g++ -Wall --std=c++11 -o bin/duel_first example/duel.cc lib/config2.a
g++: error: example/duel.cc: No such file or directory
g++: error: lib/config2.a: No such file or directory
g++: fatal error: no input files
compilation terminated.
gdeshpande@gdeshpande-18822:~$ cd ChampSim_CRC2/
gdeshpande@gdeshpande-18822:~/ChampSim_CRC2$ g++ -Wall --std=c++11 -o bin/duel_first example/duel.cc lib/config2.a
example/duel.cc:270: warning: "maxRRPV" redefined
  270 | #define maxRRPV 3
      | 
example/duel.cc:230: note: this is the location of the previous definition
  230 | #define maxRRPV 7
      | 
example/duel.cc: In function ‘int getPCCategory(uint64_t)’:
example/duel.cc:330:30: warning: comparison of integer expressions of different signedness: ‘std::vector<std::pair<long unsigned int, bool> >::size_type’ {aka ‘long unsigned int’} and ‘int’ [-Wsign-compare]
  330 |         if(alias_table.size()>ALIAS_TAB_SIZE){
      |            ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~
example/duel.cc: In function ‘void UpdateReplacementState(uint32_t, uint32_t, uint32_t, uint64_t, uint64_t, uint64_t, uint32_t, uint8_t)’:
example/duel.cc:564:35: warning: comparison of integer expressions of different signedness: ‘uint32_t’ {aka ‘unsigned int’} and ‘int’ [-Wsign-compare]
  564 |                 if(rrpv[set][way] >  (maxRRPV-4))
      |                    ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
example/duel.cc: At global scope:
example/duel.cc:728:6: error: redefinition of ‘void InitReplacementState()’
  728 | void InitReplacementState()
      |      ^~~~~~~~~~~~~~~~~~~~
example/duel.cc:366:6: note: ‘void InitReplacementState()’ previously defined here
  366 | void InitReplacementState()
      |      ^~~~~~~~~~~~~~~~~~~~
example/duel.cc:735:10: error: redefinition of ‘uint32_t GetVictimInSet(uint32_t, uint32_t, const BLOCK*, uint64_t, uint64_t, uint32_t)’
  735 | uint32_t GetVictimInSet (uint32_t cpu, uint32_t set, const BLOCK *current_set, uint64_t PC, uint64_t paddr, uint32_t type)
      |          ^~~~~~~~~~~~~~
example/duel.cc:449:10: note: ‘uint32_t GetVictimInSet(uint32_t, uint32_t, const BLOCK*, uint64_t, uint64_t, uint32_t)’ previously defined here
  449 | uint32_t GetVictimInSet (uint32_t cpu, uint32_t set, const BLOCK *current_set, uint64_t PC, uint64_t paddr, uint32_t type)
      |          ^~~~~~~~~~~~~~
example/duel.cc: In function ‘uint32_t GetVictimInSet(uint32_t, uint32_t, const BLOCK*, uint64_t, uint64_t, uint32_t)’:
example/duel.cc:738:1: warning: no return statement in function returning non-void [-Wreturn-type]
  738 | }
      | ^
example/duel.cc: At global scope:
example/duel.cc:741:6: error: redefinition of ‘void UpdateReplacementState(uint32_t, uint32_t, uint32_t, uint64_t, uint64_t, uint64_t, uint32_t, uint8_t)’
  741 | void UpdateReplacementState (uint32_t cpu, uint32_t set, uint32_t way, uint64_t paddr, uint64_t PC, uint64_t victim_addr, uint32_t type, uint8_t hit)
      |      ^~~~~~~~~~~~~~~~~~~~~~
example/duel.cc:498:6: note: ‘void UpdateReplacementState(uint32_t, uint32_t, uint32_t, uint64_t, uint64_t, uint64_t, uint32_t, uint8_t)’ previously defined here
  498 | void UpdateReplacementState (uint32_t cpu, uint32_t set, uint32_t way, uint64_t paddr, uint64_t PC, uint64_t victim_addr, uint32_t type, uint8_t hit)
      |      ^~~~~~~~~~~~~~~~~~~~~~
gdeshpande@gdeshpande-18822:~/ChampSim_CRC2$ vi example/duel.cc 
gdeshpande@gdeshpande-18822:~/ChampSim_CRC2$ g++ -Wall --std=c++11 -o bin/duel_first example/duel.cc lib/config2.a
example/duel.cc:270: warning: "maxRRPV" redefined
  270 | #define maxRRPV 3
      | 
example/duel.cc:230: note: this is the location of the previous definition
  230 | #define maxRRPV 7
      | 
example/duel.cc: In function ‘int getPCCategory(uint64_t)’:
example/duel.cc:330:30: warning: comparison of integer expressions of different signedness: ‘std::vector<std::pair<long unsigned int, bool> >::size_type’ {aka ‘long unsigned int’} and ‘int’ [-Wsign-compare]
  330 |         if(alias_table.size()>ALIAS_TAB_SIZE){
      |            ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~
example/duel.cc: In function ‘void UpdateReplacementState(uint32_t, uint32_t, uint32_t, uint64_t, uint64_t, uint64_t, uint32_t, uint8_t)’:
example/duel.cc:564:35: warning: comparison of integer expressions of different signedness: ‘uint32_t’ {aka ‘unsigned int’} and ‘int’ [-Wsign-compare]
  564 |                 if(rrpv[set][way] >  (maxRRPV-4))
      |                    ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
gdeshpande@gdeshpande-18822:~/ChampSim_CRC2$ vi run_base.sh 
gdeshpande@gdeshpande-18822:~/ChampSim_CRC2$ cp run_lime_base.sh base.sh
gdeshpande@gdeshpande-18822:~/ChampSim_CRC2$ vi base.sh 
gdeshpande@gdeshpande-18822:~/ChampSim_CRC2$ chmod +x base.sh 
gdeshpande@gdeshpande-18822:~/ChampSim_CRC2$ mkdir results/duel_first_try
gdeshpande@gdeshpande-18822:~/ChampSim_CRC2$ ./base.sh &
[1] 144
gdeshpande@gdeshpande-18822:~/ChampSim_CRC2$ Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
Running duel baseline for 10/100
./base.sh: line 7:   145 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   147 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   148 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   150 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   151 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   152 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   153 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   154 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   146 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   155 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   159 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   162 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   149 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   156 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   157 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   158 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   160 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   161 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   163 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   164 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   165 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   166 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   167 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   168 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   169 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   170 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   171 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   172 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   173 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   174 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   175 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   176 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   177 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   178 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   179 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   180 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   181 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   182 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   183 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   184 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   185 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   186 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   187 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   188 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   189 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   190 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   191 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   192 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   193 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   194 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
./base.sh: line 7:   195 Segmentation fault      (core dumped) bin/duel_first -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/duel_first_try/results_baseline_$benchmark.txt
finished running duel baseline for 10/100 million instructions
x^C
[1]+  Done                    ./base.sh
gdeshpande@gdeshpande-18822:~/ChampSim_CRC2$ client_loop: send disconnect: Broken pipe
(base) gandhardeshpande@Gandhars-MacBook-Pro ~ % ssh gdeshpande@raspi.local
gdeshpande@raspi.local's password: 
Linux raspi 5.10.92-v7l+ #1514 SMP Mon Jan 17 17:38:03 GMT 2022 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Feb 28 19:17:19 2022
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
$GPTXT,01,01,02,u-blox ag - www.u?$GPTXT,01,01,02,u-blox ag - www.u-blox.com*50

$GPTXT,01,01,02,HW  UBX-G70xx   00070000 FF7FFFFFo*69

$GPTXT,01,01,02,ROM CORE 1.00 (59842) Jun 27 2012 17:43:52*59

$GPTXT,01,01,02,PROTVER 14.00*1E

$GPTXT,01,01,02,ANTSUPERV=AC SD PDoS SR*20

$GPTXT,01,01,02,ANTSTATUS=DONTKNOW*33

$GPTXT,01,01,02,LLC FFFFFFFF-FFFFFFFF-FFFFFFFF-FFFFFFFF-FFFFFFFD*2C

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N$GPTXT,01,01,02,u-blox ag - www.u-blox.com*50

$GPTXT,01,01,02,HW  UBX-G70xx   00070000 FF7FFFFFo*69

$GPTXT,01,01,02,ROM CORE 1.00 (59842) Jun 27 2012 17:43:52*59

$GPTXT,01,01,02,PROTVER 14.00*1E

$GPTXT,01,01,02,ANTSUPERV=AC SD PDoS SR*20

$GPTXT,01,01,02,ANTSTATUS=DONTKNOW*33

$GPTXT,01,01,02,LLC FFFFFFFF-FFFFFFFF-FFFFFFFF-FFFFFFFF-FFFFFFFD*2C

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,02,ANTSTATUS=INIT*25

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,02,ANTSTATUS=OK*3B

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,02,,,17*7C

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
$GPTXT,01,01,02,ANTSTATUS=INIT*25

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,02,ANTSTATUS=OK*3B

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,01,,,24*7F

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,02,13,,,21,14,,,22*7F

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,02,13,,,21,14,,,22*7F

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,02,13,,,21,14,,,22*7F

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,02,13,,,21,14,,,21*7C

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,02,13,,,19,14,,,21*77

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,02,13,,,16,14,,,21*78

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,02,13,,,12,14,,,21*7C

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
^C
gdeshpande@raspi:~ $ sudo reboot
Connection to raspi.local closed by remote host.
Connection to raspi.local closed.
(base) gandhardeshpande@Gandhars-MacBook-Pro ~ % ssh gdeshpande@raspi.local
        

^C
(base) gandhardeshpande@Gandhars-MacBook-Pro ~ % 
(base) gandhardeshpande@Gandhars-MacBook-Pro ~ % 
(base) gandhardeshpande@Gandhars-MacBook-Pro ~ % ssh gdeshpande@raspi.local
^[[A^C
(base) gandhardeshpande@Gandhars-MacBook-Pro ~ % ssh gdeshpande@raspi.local
gdeshpande@raspi.local's password: 
Linux raspi 5.10.92-v7l+ #1514 SMP Mon Jan 17 17:38:03 GMT 2022 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Mar  1 07:38:36 2022
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
?$GPTXT,01,01,02,u-blox ag - www.u-blox.com*50

$GPTXT,01,01,02,HW  UBX-G70xx   00070000 FF7FFFFFo*69

$GPTXT,01,01,02,ROM CORE 1.00 (59842) Jun 27 2012 17:43:52*59

$GPTXT,01,01,02,PROTVER 14.00*1E

$GPTXT,01,01,02,ANTSUPERV=AC SD PDoS SR*20

$GPTXT,01,01,02,ANTSTATUS=DONTKNOW*33

$GPTXT,01,01,02,LLC FFFFFFFF-FFFFFFFF-FFFFFFFF-FFFFFFFF-FFFFFFFD*2C

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,02,ANTSTATUS=INIT*25

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*?$GPTXT,01,01,02,u-blox ag - www.u-blox.com*50

$GPTXT,01,01,02,HW  UBX-G70xx   00070000 FF7FFFFFo*69

$GPTXT,01,01,02,ROM CORE 1.00 (59842) Jun 27 2012 17:43:52*59

$GPTXT,01,01,02,PROTVER 14.00*1E

$GPTXT,01,01,02,ANTSUPERV=AC SD PDoS SR*20

$GPTXT,01,01,02,ANTSTATUS=DONTKNOW*33

$GPTXT,01,01,02,LLC FFFFFFFF-FFFFFFFF-FFFFFFFF-FFFFFFFF-FFFFFFFD*2C

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99??$GPTXT,01,01,02,u-blox ag - www.u-blox.com*50

$GPTXT,01,01,02,HW  UBX-G70xx   00070000 FF7FFFFFo*69

$GPTXT,01,01,02,ROM CORE 1.00 (59842) Jun 27 2012 17:43:52*59

$GPTXT,01,01,02,PROTVER 14.00*1E

$GPTXT,01,01,02,ANTSUPERV=AC SD PDoS SR*20

$GPTXT,01,01,02,ANTSTATUS=DONTKNOW*33

$GPTXT,01,01,02,LLC FFFFFFFF-FFFFFFFF-FFFFFFFF-FFFFFFFF-FFFFFFFD*2C

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,02,ANTSTATUS=INIT*25

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,02,ANTSTATUS=OK*3B

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
?$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,21*78

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,20*79

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,20*79

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,21*78

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,20*79

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,20*79

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,20*79

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,19*73

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,19*73

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,19*73

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,19*73

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,20*79

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,22*7B

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,23*7A

$GPGLL,,,,,,V,N*64

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,01,03,,,23*7A

$GPGLL,,,,,,V,N*64

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
VKKKKKKNN)?b??r??b??r??R??jR":A11??????Y?9???5)?$GPTXT,01,01,02,ANTSTATUS=OK*3B

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
±????XXXXXTl?5)?AM??ű??????????????????????????5)?AMY?űű?ɱ?ѱ???ݱ?山?????5)?A11??????????չ?ݱY?9???5)?$GPRMC,155747.00,V,,,,,,,010322,,,N*7A

$GPVTG,,,,,,,,,N*30

$GPGGA,155747.00,,,,,0,00,99.99,,,,,,*63

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,02,04,,,27,09,,,28*79

$GPGLL,,,,,155747.00,V,N*4F

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,155748.00,V,,,,,,,010322,,,N*75

$GPVTG,,,,,,,,,N*30

$GPGGA,155748.00,,,,,0,00,99.99,,,,,,*6C

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,02,04,,,27,09,,,28*79

$GPGLL,,,,,155748.00,V,N*40

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,155749.00,V,,,,,,,010322,,,N*74

$GPVTG,,,,,,,,,N*30

$GPGGA,155749.00,,,,,0,00,99.99,,,,,,*6D

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,1,1,02,04,,,27,09,,,28*79

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
?$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPRMC,,V,,,,,,,,,,N*53

$GPVTG,,,,,,,,,N*30

$GPGGA,,,,,,0,00,99.99,,,,,,*48

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGLL,,,,,,V,N*64

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

^C
gdeshpande@raspi:~ $ cat /dev/ttys1
cat: /dev/ttys1: No such file or directory
gdeshpande@raspi:~ $ cat /dev/ttys0
cat: /dev/ttys0: No such file or directory
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
?$GPRMC,155933.00,V,,,,,,,010322,,,N*77

$GPVTG,,,,,,,,,N*30

$GPGGA,155933.00,,,,,0,00,99.99,,,,,,*6E

$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30

$GPGSV,2,1,06,03,33,181,20,04,67,071,33,07,,,29,09,60,333,32*47

$GPGSV,2,2,06,26,09,041,16,51,50,162,35*72

$GPGLL,,,,,155933.00,V,N*42

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

$GPTXT,01,01,01,NMEA unknown msg*58

^C
gdeshpande@raspi:~ $ stty -F /dev/ttyAMA0 -echo
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
$GPRMC,160012.00,V,,,,,,,010322,,,N*7B

$GPVTG,,,,,,,,,N*30

$GPGGA,160012.00,,,,,0,05,4.66,,,,,,*53

$GPGSA,A,1,03,04,09,51,07,,,,,,,,12.63,4.66,11.74*0C

$GPGSV,2,1,07,03,32,181,24,04,67,072,30,07,41,278,29,09,61,333,32*7A

$GPGSV,2,2,07,26,09,041,,46,50,201,30,51,50,162,35*43

$GPGLL,,,,,160012.00,V,N*4E

$GPRMC,160013.00,V,,,,,,,010322,,,N*7A

$GPVTG,,,,,,,,,N*30

$GPGGA,160013.00,,,,,0,05,4.66,,,,,,*52

$GPGSA,A,1,03,04,09,51,07,,,,,,,,12.62,4.66,11.73*0A

$GPGSV,2,1,08,03,32,181,25,04,67,072,30,06,03,269,,07,41,278,29*70

$GPGSV,2,2,08,09,61,333,32,26,09,041,,46,50,201,30,51,50,162,35*70

$GPGLL,,,,,160013.00,V,N*4F

$GPRMC,160014.00,V,,,,,,,010322,,,N*7D

$GPVTG,,,,,,,,,N*30

$GPGGA,160014.00,,,,,0,05,4.65,,,,,,*56

$GPGSA,A,1,03,04,09,51,07,,,,,,,,12.61,4.65,11.72*0B

$GPGSV,2,1,08,03,32,181,26,04,67,072,30,06,03,269,,07,41,278,29*73

$GPGSV,2,2,08,09,61,333,32,26,09,041,,46,50,201,30,51,50,162,35*70

$GPGLL,,,,,160014.00,V,N*48

$GPRMC,160015.00,V,,,,,,,010322,,,N*7C

$GPVTG,,,,,,,,,N*30

$GPGGA,160015.00,,,,,0,05,4.65,,,,,,*57

$GPGSA,A,1,03,04,09,51,07,,,,,,,,12.60,4.65,11.71*09

$GPGSV,2,1,08,03,32,181,27,04,67,072,30,06,03,269,,07,41,278,28*73

$GPGSV,2,2,08,09,61,333,31,26,09,041,,46,50,201,29,51,50,162,35*7B

$GPGLL,,,,,160015.00,V,N*49

$GPRMC,160016.00,V,,,,,,,010322,,,N*7F

$GPVTG,,,,,,,,,N*30

$GPGGA,160016.00,,,,,0,05,4.65,,,,,,*54

$GPGSA,A,1,03,04,09,51,07,,,,,,,,12.60,4.65,11.71*09

$GPGSV,2,1,08,03,32,181,28,04,67,072,30,06,03,269,,07,41,278,28*7C

$GPGSV,2,2,08,09,61,333,31,26,09,041,,46,50,201,29,51,50,162,35*7B

$GPGLL,,,,,160016.00,V,N*4A

$GPRMC,160017.00,V,,,,,,,010322,,,N*7E

$GPVTG,,,,,,,,,N*30

$GPGGA,160017.00,,,,,0,05,4.65,,,,,,*55

$GPGSA,A,1,03,04,09,51,07,,,,,,,,12.59,4.65,11.70*02

$GPGSV,2,1,08,03,32,181,28,04,67,072,30,06,03,269,,07,41,278,27*73

$GPGSV,2,2,08,09,61,333,31,26,09,041,,46,50,201,29,51,50,162,35*7B

$GPGLL,,,,,160017.00,V,N*4B

^C
gdeshpande@raspi:~ $ cat /dev/ttyAMA0
,,07,41,278,28*76

$GPGSV,2,2,08,09,61,333,33,26,09,041,17,46,50,201,31,51,50,162,36*75

$GPGLL,,,,,160026.00,V,N*49

$GPRMC,160027.00,V,,,,,,,010322,,,N*7D

$GPVTG,,,,,,,,,N*30

$GPGGA,160027.00,,,,,0,05,4.63,,,,,,0000*50

$GPGSA,A,1,03,04,09,51,07,,,,,,,,12.51,4.63,11.62*0F

$GPGSV,2,1,08,03,32,181,33,04,67,072,30,06,03,269,,07,41,278,28*76

$GPGSV,2,2,08,09,61,333,32,26,09,041,15,46,50,201,31,51,50,162,36*76

$GPGLL,,,,,160027.00,V,N*48

$GPRMC,160028.00,A,3252.46861,N,11713.25423,W,0.033,,010322,,,D*64

$GPVTG,,T,,M,0.033,N,0.061,K,D*21

$GPGGA,160028.00,3252.46861,N,11713.25423,W,2,05,4.63,391.5,M,-33.8,M,,0000*63

$GPGSA,A,3,03,04,09,51,07,,,,,,,,12.50,4.63,11.61*0F

$GPGSV,2,1,08,03,32,181,33,04,67,072,30,06,03,269,,07,41,278,29*77

$GPGSV,2,2,08,09,61,333,33,26,09,041,13,46,50,201,31,51,50,162,36*71

$GPGLL,3252.46861,N,11713.25423,W,160028.00,A,D*7F

$GPRMC,160029.00,A,3252.46937,N,11713.25331,W,0.058,,010322,,,D*6E

$GPVTG,,T,,M,0.058,N,0.107,K,D*2D

$GPGGA,160029.00,3252.46937,N,11713.25331,W,2,05,4.62,385.3,M,-33.8,M,,0000*66

$GPGSA,A,3,03,04,09,51,07,,,,,,,,12.49,4.62,11.60*07

$GPGSV,2,1,08,03,32,181,33,04,67,072,30,06,03,269,,07,41,278,28*76

$GPGSV,2,2,08,09,61,333,32,26,09,041,12,46,50,201,30,51,50,162,35*73

$GPGLL,3252.46937,N,11713.25331,W,160029.00,A,D*78

$GPRMC,160030.00,A,3252.47007,N,11713.25247,W,0.114,,010322,,,D*64

$GPVTG,,T,,M,0.114,N,0.211,K,D*20

$GPGGA,160030.00,3252.47007,N,11713.25247,W,2,05,4.62,379.7,M,-33.8,M,,0000*62

$GPGSA,A,3,03,04,09,51,07,,,,,,,,12.48,4.62,11.59*0C

$GPGSV,2,1,08,03,32,181,33,04,67,073,30,06,03,269,,07,41,278,28*77

$GPGSV,2,2,08,09,61,333,32,26,09,041,09,46,50,201,30,51,50,162,35*79

$GPGLL,3252.47007,N,11713.25247,W,160030.00,A,D*7B

$GPRMC,160031.00,A,3252.47038,N,11713.25215,W,0.015,,010322,,,D*6E

$GPVTG,,T,,M,0.015,N,0.028,K,D*28

$GPGGA,160031.00,3252.47038,N,11713.25215,W,2,05,4.62,376.9,M,-33.8,M,,0000*69

$GPGSA,A,3,03,04,09,51,07,,,,,,,,12.47,4.62,11.59*03

$GPGSV,2,1,08,03,32,181,32,04,67,073,30,06,03,269,,07,41,278,29*77

$GPGSV,2,2,08,09,61,333,32,26,09,041,12,46,50,201,31,51,50,162,33*74

$GPGLL,3252.47038,N,11713.25215,W,160031.00,A,D*71

$GPRMC,160032.00,A,3252.47084,N,11713.25158,W,0.035,,010322,,,D*62

$GPVTG,,T,,M,0.035,N,0.065,K,D*23

$GPGGA,160032.00,3252.47084,N,11713.25158,W,2,05,4.62,373.5,M,-33.8,M,,0000*6E

$GPGSA,A,3,03,04,09,51,07,,,,,,,,12.46,4.62,11.58*03

$GPGSV,2,1,08,03,32,181,32,04,67,073,30,06,03,268,,07,41,278,28*77

$GPGSV,2,2,08,09,61,333,32,26,09,041,14,46,50,201,31,51,50,162,36*77

$GPGLL,3252.47084,N,11713.25158,W,160032.00,A,D*7F

$GPRMC,160033.00,A,3252.47107,N,11713.25143,W,0.097,,010322,,,D*6B

$GPVTG,,T,,M,0.097,N,0.180,K,D*21

$GPGGA,160033.00,3252.47107,N,11713.25143,W,2,05,4.62,371.4,M,-33.8,M,,0000*6C

$GPGSA,A,3,03,04,09,51,07,,,,,,,,12.46,4.62,11.57*0C

$GPGSV,2,1,08,03,32,181,32,04,67,073,30,06,03,268,,07,41,278,28*77

$GPGSV,2,2,08,09,61,333,32,26,09,041,13,46,50,201,30,51,50,162,36*71

$GPGLL,3252.47107,N,11713.25143,W,160033.00,A,D*7E

^C
gdeshpande@raspi:~ $ cd Desktop/
gdeshpande@raspi:~/Desktop $ ls
gps
gdeshpande@raspi:~/Desktop $ cd gps/
gdeshpande@raspi:~/Desktop/gps $ ls
testing.py
gdeshpande@raspi:~/Desktop/gps $ python testing.py 
NMEA Time:  160105.00 

NMEA Latitude: 3252.47496 NMEA Longitude: 11713.24790 

lat in degrees: 32.8746  long in degree:  117.2208 

http://maps.google.com/?q=32.8746,117.2208
------------------------------------------------------------

NMEA Time:  160106.00 

NMEA Latitude: 3252.47524 NMEA Longitude: 11713.24761 

lat in degrees: 32.8746  long in degree:  117.2208 

http://maps.google.com/?q=32.8746,117.2208
------------------------------------------------------------

NMEA Time:  160107.00 

NMEA Latitude: 3252.47551 NMEA Longitude: 11713.24732 

lat in degrees: 32.8746  long in degree:  117.2208 

http://maps.google.com/?q=32.8746,117.2208
------------------------------------------------------------

NMEA Time:  160108.00 

NMEA Latitude: 3252.47582 NMEA Longitude: 11713.24698 

lat in degrees: 32.8746  long in degree:  117.2208 

http://maps.google.com/?q=32.8746,117.2208
------------------------------------------------------------

NMEA Time:  160109.00 

NMEA Latitude: 3252.47605 NMEA Longitude: 11713.24681 

lat in degrees: 32.8746  long in degree:  117.2208 

http://maps.google.com/?q=32.8746,117.2208
------------------------------------------------------------

NMEA Time:  160110.00 

NMEA Latitude: 3252.47630 NMEA Longitude: 11713.24656 

lat in degrees: 32.8746  long in degree:  117.2208 

http://maps.google.com/?q=32.8746,117.2208
------------------------------------------------------------

NMEA Time:  160111.00 

NMEA Latitude: 3252.47650 NMEA Longitude: 11713.24632 

lat in degrees: 32.8746  long in degree:  117.2208 

http://maps.google.com/?q=32.8746,117.2208
------------------------------------------------------------

NMEA Time:  160112.00 

NMEA Latitude: 3252.47676 NMEA Longitude: 11713.24605 

lat in degrees: 32.8746  long in degree:  117.2208 

http://maps.google.com/?q=32.8746,117.2208
------------------------------------------------------------

NMEA Time:  160113.00 

NMEA Latitude: 3252.47705 NMEA Longitude: 11713.24577 

lat in degrees: 32.8746  long in degree:  117.2208 

http://maps.google.com/?q=32.8746,117.2208
------------------------------------------------------------

^Cgdeshpande@raspi:~/Desktop/gps $ vi testing.py 
gdeshpande@raspi:~/Desktop/gps $ 
gdeshpande@raspi:~/Desktop/gps $ vi test2.py
gdeshpande@raspi:~/Desktop/gps $ python test2.py 
  File "/home/gdeshpande/Desktop/gps/test2.py", line 2
    Import time
           ^
SyntaxError: invalid syntax
gdeshpande@raspi:~/Desktop/gps $ vi test2.py
gdeshpande@raspi:~/Desktop/gps $ nano test2.py 
gdeshpande@raspi:~/Desktop/gps $ python test2.py 
  File "/home/gdeshpande/Desktop/gps/test2.py", line 3
    import string import pynmea2
                  ^
SyntaxError: invalid syntax
gdeshpande@raspi:~/Desktop/gps $ nano test2.py 
gdeshpande@raspi:~/Desktop/gps $ nano test2.py 
gdeshpande@raspi:~/Desktop/gps $ python test2.py 
  File "/home/gdeshpande/Desktop/gps/test2.py", line 6
    while True: port=“/dev/ttyAMAO”
                     ^
SyntaxError: invalid character '“' (U+201C)
gdeshpande@raspi:~/Desktop/gps $ python testing.py 
NMEA Time:  160935.00 

NMEA Latitude: 3252.49678 NMEA Longitude: 11713.22615 

lat in degrees: 32.8749  long in degree:  117.2204 

http://maps.google.com/?q=32.8749,117.2204
------------------------------------------------------------

NMEA Time:  160936.00 

NMEA Latitude: 3252.49683 NMEA Longitude: 11713.22613 

lat in degrees: 32.8749  long in degree:  117.2204 

http://maps.google.com/?q=32.8749,117.2204
------------------------------------------------------------

NMEA Time:  160937.00 

NMEA Latitude: 3252.49686 NMEA Longitude: 11713.22613 

lat in degrees: 32.8749  long in degree:  117.2204 

http://maps.google.com/?q=32.8749,117.2204
------------------------------------------------------------

NMEA Time:  160938.00 

NMEA Latitude: 3252.49690 NMEA Longitude: 11713.22612 

lat in degrees: 32.8749  long in degree:  117.2204 

http://maps.google.com/?q=32.8749,117.2204
------------------------------------------------------------

^Cgdeshpande@raspi:~/Desktop/gps $ vi testing.py 

'''
GPS Interfacing with Raspberry Pi using Pyhton
http://www.electronicwings.com
'''
import serial               #import serial pacakge
from time import sleep
import webbrowser           #import package for opening link in browser
import sys                  #import system package

def GPS_Info():
    global NMEA_buff
    global lat_in_degrees
    global long_in_degrees
    nmea_time = []
    nmea_latitude = []
    nmea_longitude = []
    nmea_time = NMEA_buff[0]                    #extract time from GPGGA string
    nmea_latitude = NMEA_buff[1]                #extract latitude from GPGGA string
    nmea_longitude = NMEA_buff[3]               #extract longitude from GPGGA string

    print("NMEA Time: ", nmea_time,'\n')
    print ("NMEA Latitude:", nmea_latitude,"NMEA Longitude:", nmea_longitude,'\n')

    lat = float(nmea_latitude)                  #convert string into float for calculation
    longi = float(nmea_longitude)               #convertr string into float for calculation

    lat_in_degrees = convert_to_degrees(lat)    #get latitude in degree decimal format
    long_in_degrees = convert_to_degrees(longi) #get longitude in degree decimal format

#convert raw NMEA string into degree decimal format
def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position



gpgga_info = "$GPGGA,"
ser = serial.Serial ("/dev/serial0")              #Open port with baud rate
GPGGA_buffer = 0
NMEA_buff = 0
lat_in_degrees = 0
long_in_degrees = 0

try:
    while True:
        received_data = (str)(ser.readline())                   #read NMEA string received
        GPGGA_data_available = received_data.find(gpgga_info)   #check for NMEA GPGGA string
        if (GPGGA_data_available>0):
            GPGGA_buffer = received_data.split("$GPGGA,",1)[1]  #store data coming after "$GPGGA," string
            NMEA_buff = (GPGGA_buffer.split(','))               #store comma separated data in buffer
            GPS_Info()                                          #get time, latitude, longitude

            print("lat in degrees:", lat_in_degrees," long in degree: ", long_in_degrees, '\n')
            map_link = 'http://maps.google.com/?q=' + lat_in_degrees + ',' + long_in_degrees    #create link to plot location on Google map
            print(map_link)               #press ctrl+c to plot on map and exit
            print("------------------------------------------------------------\n")
except KeyboardInterrupt:
    sys.exit(0)
"testing.py" 62 lines, 2678 bytes
