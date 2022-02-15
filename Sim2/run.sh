#!/bin/bash

while read benchmark; do 
    echo "Running $benchmark for lime with 5 trainers and  64 history"
    bin/lime_dse/lime5_64 -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/lime_size/lime5_64/result_baseline_$benchmark.txt &
done < benchmarks_all.txt
wait

while read benchmark; do 
    echo "Running $benchmark for lime with 5 trainers and 128 history"
    bin/lime_dse/lime5_128 -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/lime_size/lime5_128/result_baseline_$benchmark.txt &
done < benchmarks_all.txt
wait

while read benchmark; do 
    echo "Running $benchmark for lime with 5 trainers and  256 history"
    bin/lime_dse/lime5_256 -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/lime_size/lime5_256/result_baseline_$benchmark.txt &
done < benchmarks_all.txt
wait

while read benchmark; do 
    echo "Running $benchmark for lime with 20 trainers and  64 history"
    bin/lime_dse/lime20_64 -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/lime_size/lime20_64/result_baseline_$benchmark.txt &
done < benchmarks_all.txt
wait

while read benchmark; do 
    echo "Running $benchmark for lime with 20 trainers and  256 history"
    bin/lime_dse/lime20_256 -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/lime_size/lime20_256/result_baseline_$benchmark.txt &
done < benchmarks_all.txt
wait

while read benchmark; do 
    echo "Running $benchmark for lime with 40 trainers and  64 history"
    bin/lime_dse/lime40_64 -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/lime_size/lime40_64/result_baseline_$benchmark.txt &
done < benchmarks_all.txt
wait

while read benchmark; do 
    echo "Running $benchmark for lime with 40 trainers and  128 history"
    bin/lime_dse/lime40_128 -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/lime_size/lime40_128/result_baseline_$benchmark.txt &
done < benchmarks_all.txt
wait

while read benchmark; do 
    echo "Running $benchmark for lime with 40 trainers and 256 history"
    bin/lime_dse/lime40_256 -warmup_instructions 10000000 -simulation_instructions 100000000 -traces /datasets/cs240c-wi22-a00-public/data/Assignment2-gz/$benchmark > results/lime_size/lime40_256/result_baseline_$benchmark.txt &
done < benchmarks_all.txt
wait

