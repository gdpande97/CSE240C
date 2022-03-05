import os
import matplotlib.pyplot as plt
from scipy.stats import gmean
from statistics import mean
import csv


results_dir = "./results"
previous_dir = "./../"
images_dir = "./images/"

#create a results array:
result_arr = []

#setup csv file for results:
result_file_csv = "results_total.csv"
header_row = ['Model', 'trace name', 'IPC', 'number of instructions', 'number of load misses', 'MPKI']
final_result_file = open(result_file_csv, 'w')

#open csv writer and write header file
writer = csv.writer(final_result_file)
writer.writerow(header_row)


ipc_model_results = {}
mpki_model_results = {}

#open results directory:
os.chdir(results_dir)

#enter each directory inside results:
count = 0
for subdir in os.listdir():
    
    os.chdir(subdir)
    #for each subdirectory enter particular model directory:
    for model in os.listdir():
        #enter every folder and read result files:
        os.chdir(model)
        model_ipc = []
        model_mpki = []
        for file in os.listdir():
            result_file = open(file, 'r')
            lines = result_file.readlines()
            #go through the lines to find IPC and MPKI
            csv_row = []
            csv_row.append(model)
            csv_row.append(file)
            for line in lines:
                if line.find('Finished') != -1:
                    #find ipc:
                    ipc_start = line.find('IPC:')
                    ipc_end = line.find('(Simulation')
                    ipc_val = float(line[ipc_start+4:ipc_end])
                    csv_row.append(ipc_val)
                    model_ipc.append(ipc_val)
                    #find number of instructions
                    instructions_start = line.find('instructions:')
                    instructions_end = line.find('cycles:')
                    instructions_val = float(line[instructions_start+13: instructions_end])
                    csv_row.append(instructions_val)
                if line.find('LLC TOTAL') != -1:
                    #find number of misses:
                    misses_start = line.find('MISS:')
                    misses_val = float(line[misses_start + 5:-1])
                    csv_row.append(misses_val)
                    #compute MPKI
                    mpki_val = (misses_val * 1000 /csv_row[3])
                    csv_row.append(mpki_val)
                    model_mpki.append(mpki_val)
            #write all values into csv
            writer.writerow(csv_row)
            result_arr.append(csv_row)
        
        ipc_model_results[model] = model_ipc
        mpki_model_results[model] = model_mpki
        os.chdir(previous_dir)

    os.chdir(previous_dir)

os.chdir(previous_dir)

os.chdir(images_dir)

#IPC geomean structures
ipc_geomean_map = {}
mpki_mean_map = {}

#compute and add data for geomean for every model
for key in ipc_model_results:
    ipc_geomean = gmean(ipc_model_results[key])
    ipc_geomean_map[key] = ipc_geomean

mpki_reduction = []

for key in mpki_model_results:
    mpki_mean = mean(mpki_model_results[key])
    mpki_mean_map[key] = mpki_mean

# print("SHIP C1 IPC: " + str(ipc_geomean_map['baseline_ship_c1']))
# print("LRU C1 IPC: " + str(ipc_geomean_map['baseline_lru_c1']))

# print("SHIP C1 MPKI: " + str(mpki_mean_map['baseline_ship_c1']))
# print("LRU C1 MPKI: " + str(mpki_mean_map['baseline_lru_c1']))


print("SHIP IPC: " + str(ipc_geomean_map['ship_redo']/ipc_geomean_map['baseline_lru_ship']))
print("SHIP MPKI: " + str(mpki_mean_map['ship_redo']))

print("LIME IPC: " + str(ipc_geomean_map['lime_redo']/ipc_geomean_map['baseline_lru_ship']))
print("LIME MPKI: " + str(mpki_mean_map['lime_redo']))

print("baseline IPC: " + str(ipc_geomean_map['baseline_lru_ship']))
print("baseline MPKI: " + str(mpki_mean_map['baseline_lru_ship']))

print("duel c2 v8 IPC: " + str(ipc_geomean_map['baseline_duel_c2_8']))
print("duel c2 v8 MPKI: " + str(mpki_mean_map['baseline_duel_c2_8']))

print("duel c2 v8.2 IPC: " + str(ipc_geomean_map['baseline_duel_c2_8_2']))
print("duel c2 v8.2 MPKI: " + str(mpki_mean_map['baseline_duel_c2_8_2']))

print("duel c2 v8.3 IPC: " + str(ipc_geomean_map['baseline_duel_c2_8_3']))
print("duel c2 v8.3 MPKI: " + str(mpki_mean_map['baseline_duel_c2_8_3']))

print("duel c2 v8.4 IPC: " + str(ipc_geomean_map['baseline_duel_c2_8_4']/ipc_geomean_map['baseline_lru_ship']))
print("duel c2 v8.4 MPKI: " + str(mpki_mean_map['baseline_duel_c2_8_4']))

print("duel v2 IPC: " + str(ipc_geomean_map['baseline_duel_v2']))
print("duel v2 MPKI: " + str(mpki_mean_map['baseline_duel_v2']))

print("duel 1024 IPC: " + str(ipc_geomean_map['baseline_duel_1024']))
print("duel 1024 MPKI: " + str(mpki_mean_map['baseline_duel_1024']))

print("duel 256 IPC: " + str(ipc_geomean_map['baseline_duel_256']))
print("duel 256 MPKI: " + str(mpki_mean_map['baseline_duel_256']))

print("duel 32 IPC: " + str(ipc_geomean_map['baseline_duel_32']))
print("duel 32 MPKI: " + str(mpki_mean_map['baseline_duel_32']))

print("duel 96 IPC: " + str(ipc_geomean_map['baseline_duel_96']))
print("duel 96 MPKI: " + str(mpki_mean_map['baseline_duel_96']))

print("duel 128 IPC: " + str(ipc_geomean_map['baseline_duel_128']))
print("duel 128 MPKI: " + str(mpki_mean_map['baseline_duel_128']))


set_exp = ['baseline_duel_32', 'baseline_duel_c2_8_4', 'baseline_duel_96', 'baseline_duel_128']
set_x = ['32', '64', '96', '128']
set_results = []
for key in set_exp:
    set_results.append(ipc_geomean_map[key])

fig1, ax = plt.subplots()
ax.set_xlabel("Number of sets")
ax.set_ylabel("IPC")
ax.set_title("Variation of performance with set numbers")
set_final = ax.plot(set_x, set_results)
plt.savefig("IPC_sets_dyn.png")

sel_exp = ['baseline_duel_256', 'baseline_duel_c2_8_4', 'baseline_duel_1024', 'baseline_duel_2048']
sel_x = [512, 1024, 2048, 4096]
sel_results = []
for key in sel_exp:
    sel_results.append(ipc_geomean_map[key])

fig1, ax = plt.subplots()
ax.set_xlabel("Selection Counter Size")
ax.set_ylabel("IPC")
set_final = ax.plot(sel_x, sel_results)
ax.set_title("Variation of performance with select counter numbers")
plt.savefig("IPC_sel_dyn.png")



lime_tag_models = ['lime_tag_28', 'lime_tag_30', 'lime_tag_32', 'lime34', 'lime35', 'lime36', 'baseline_lime_paper', 'lime38', 'lime39', 'lime40']
lime_tag_x = [28, 30, 32, 34, 35, 36, 37, 38, 39, 40]
tag_results = []
tag_mpki = []
for key in lime_tag_models:
    # tag_results.append(ipc_geomean_map[key])
    tag_results.append(ipc_geomean_map[key])
    tag_mpki.append(mpki_mean_map[key])

fig4, ax = plt.subplots()
ax.set_xlabel("Max Tag Hash")
ax.set_ylabel("Normalized IPC")
tag_ipc = ax.plot(lime_tag_x, tag_results)

plt.savefig('lime_tag_ipc.png')

plt.show()