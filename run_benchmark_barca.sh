#!/bin/bash

while read benchmark; do 
    echo "Running $benchmark for barca with 8 sets"
    ./run_champsim.sh hashed_perceptron-barca_8sets-next_line-spp_dev-no-lru-1core 50 50 $benchmark
done < benchmarks.txt

mv results_50M/ results_barca_8sets/

while read benchmark; do 
    echo "Running $benchmark for barca with 32 sets"
    ./run_champsim.sh hashed_perceptron-barca_32sets-next_line-spp_dev-no-lru-1core 50 50 $benchmark
done < benchmarks.txt

mv results_50M/ results_barca_32sets/

while read benchmark; do 
    echo "Running $benchmark for barca with 128 sets"
    ./run_champsim.sh hashed_perceptron-barca_128sets-next_line-spp_dev-no-lru-1core 50 50 $benchmark
done < benchmarks.txt

mv results_50M/ results_barca_128sets/

while read benchmark; do 
    echo "Running $benchmark for barca with 512 sets"
    ./run_champsim.sh hashed_perceptron-barca_512sets-next_line-spp_dev-no-lru-1core 50 50 $benchmark
done < benchmarks.txt

mv results_50M/ results_barca_512sets/

while read benchmark; do 
    echo "Running $benchmark for barca with 2048 sets"
    ./run_champsim.sh hashed_perceptron-barca_2048sets-next_line-spp_dev-no-lru-1core 50 50 $benchmark
done < benchmarks.txt

mv results_50M/ results_barca_2048sets/
