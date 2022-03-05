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

print(os.getcwd())
#we have finished extracting all meaningful data, now we start creating data structures for computing and storing results:

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



# baseline_models = ['baseline_lru_ship', 'baseline_ship_paper', 'baseline_lime_paper', 'lime_redo', 'ship_redo']

# for key in baseline_models:
#     print("model: " + key + " IPC: " + str(ipc_geomean_map[key]))
#     print("normalized IPC gain: " + str(ipc_geomean_map[key]/ipc_geomean_map['baseline_lru_ship']))
#     print("model: " + key + " MPKI: " + str(mpki_mean_map[key]))
#     print("normalized MPKI reduction on an average: " + str(mpki_mean_map[key] - mpki_mean_map['baseline_lru_ship']))


#SHIP RRPV models
ship_rrpv_models = ['ship2', 'baseline_ship_paper', 'ship4', 'ship5', 'ship6', 'ship7']
ship_rrpv_x = [2, 3, 4, 5, 6, 7]
rrpv_results = []
rrpv_mpki = []

for key in ship_rrpv_models:
    # rrpv_results.append(ipc_geomean_map[key])
    rrpv_results.append(ipc_geomean_map[key]/ipc_geomean_map['baseline_lru_ship'])
    rrpv_mpki.append(mpki_mean_map[key])

#SHIP Sets
ship_set_models = ['ship16', 'ship32','ship48', 'baseline_ship_paper', 'ship80', 'ship96', 'ship112', 'ship128']
ship_set_x = [16, 32, 48, 64, 80, 96, 112, 128]
set_results = []
set_mpki = []

for key in ship_set_models:
    # set_results.append(ipc_geomean_map[key])
    set_results.append(ipc_geomean_map[key]/ipc_geomean_map['baseline_lru_ship'])
    set_mpki.append(mpki_mean_map[key])

#LIME PC hash
lime_pc_models = ['lime14', 'lime15', 'lime16', 'lime17', 'baseline_lime_paper', 'lime19', 'lime20', 'lime21', 'lime22']
lime_pc_x = [14, 15, 16, 17, 18, 19, 20, 21, 22]
pc_results = []
pc_mpki = []
for key in lime_pc_models:
    # pc_results.append(ipc_geomean_map[key])
    pc_results.append(ipc_geomean_map[key]/ipc_geomean_map['baseline_lru_ship'])
    pc_mpki.append(mpki_mean_map[key])

#LIME tag hash
lime_tag_models = ['lime_tag_28', 'lime_tag_30', 'lime34', 'lime35', 'lime36', 'baseline_lime_paper', 'lime38', 'lime39', 'lime40']
lime_tag_x = [28, 30, 34, 35, 36, 37, 38, 39, 40]
tag_results = []
tag_mpki = []
for key in lime_tag_models:
    # tag_results.append(ipc_geomean_map[key])
    tag_results.append(ipc_geomean_map[key]/ipc_geomean_map['baseline_lru_ship'])
    tag_mpki.append(mpki_mean_map[key])

ship_size_models = ['ship12', 'ship13', 'baseline_ship_paper', 'ship15', 'ship16', 'ship17', 'ship18']
ship_size_x = [12, 13, 14, 15, 16, 17, 18]
ship_size_results = []
ship_size_mpki = []
for key in ship_size_models:
    # ship_size_results.append(ipc_geomean_map[key])
    ship_size_results.append(ipc_geomean_map[key]/ipc_geomean_map['baseline_lru_ship'])
    ship_size_mpki.append(mpki_mean_map[key])

lime_size_models = ['lime5_64', 'lime20_64', 'lime40_64', 'lime5_128', 'baseline_lime_paper', 'lime40_128', 'lime5_256', 'lime20_256', 'lime40_256']
lime_size_x = ['5, 64', '20, 64', '40, 64', '5, 128', '20, 128', '40, 128', '5, 256', '20, 256', '40, 256']
lime_size_results = []
lime_size_mpki = []
for key in lime_size_models:
    # lime_size_results.append(ipc_geomean_map[key])
    lime_size_results.append(ipc_geomean_map[key]/ipc_geomean_map['baseline_lru_ship'])
    lime_size_mpki.append(mpki_mean_map[key])


fig1, ax = plt.subplots()
ax.set_xlabel("Max RRPV Value")
ax.set_ylabel("Normalized IPC")
rrpv_ipc = ax.plot(ship_rrpv_x, rrpv_results)

plt.savefig('ship_rrpv_ipc.png')

# for r in rrpv_ipc:
#     height = r.get_height()
#     ax.annotate('{}'.format(height),
#       xy=(r.get_x() + r.get_width() / 2, height),
#       xytext=(0, 3), # 3 points vertical offset
#       textcoords="offset points",
#       ha='center', va='bottom')


fig2, ax = plt.subplots()
ax.set_xlabel("Max Number of Sets")
ax.set_ylabel("Normalized IPC")
sets_ipc = ax.plot(ship_set_x, set_results)

plt.savefig('ship_sets_ipc.png')
# for r in sets_ipc:
#     height = r.get_height()
#     ax.annotate('{}'.format(height),
#       xy=(r.get_x() + r.get_width() / 2, height),
#       xytext=(0, 3), # 3 points vertical offset
#       textcoords="offset points",
#       ha='center', va='bottom')



fig3, ax = plt.subplots()
ax.set_xlabel("Max PC Hash")
ax.set_ylabel("Normalized IPC")
pc_ipc = ax.plot(lime_pc_x, pc_results)

plt.savefig('lime_pc_ipc.png')
# for r in pc_ipc:
#     height = r.get_height()
#     ax.annotate('{}'.format(height),
#       xy=(r.get_x() + r.get_width() / 2, height),
#       xytext=(0, 3), # 3 points vertical offset
#       textcoords="offset points",
#       ha='center', va='bottom')

fig4, ax = plt.subplots()
ax.set_xlabel("Max Tag Hash")
ax.set_ylabel("Normalized IPC")
tag_ipc = ax.plot(lime_tag_x, tag_results)

plt.savefig('lime_tag_ipc.png')
# for r in tag_ipc:
#     height = r.get_height()
#     ax.annotate('{}'.format(height),
#       xy=(r.get_x() + r.get_width() / 2, height),
#       xytext=(0, 3), # 3 points vertical offset
#       textcoords="offset points",
#       ha='center', va='bottom')


fig5, ax = plt.subplots()
ax.set_xlabel("RRPV Max Value")
ax.set_ylabel("Average MPKI")
mpki_rrpv = ax.plot(ship_rrpv_x, rrpv_mpki)

plt.savefig('ship_rrpv_mpki.png')


fig6, ax = plt.subplots()
ax.set_xlabel("Number of sets")
ax.set_ylabel("Average MPKI")
mpki_ssets = ax.plot(ship_set_x, set_mpki)

plt.savefig('ship_sets_mpki.png')

fig7, ax = plt.subplots()
ax.set_xlabel("PC Hash Bits")
ax.set_ylabel("Average MPKI")
mpki_pc = ax.plot(lime_pc_x, pc_mpki)


plt.savefig('lime_pc_mpki.png')

fig8, ax = plt.subplots()
ax.set_xlabel("Tag Hash Bits")
ax.set_ylabel("Average MPKI")
mpki_tag = ax.plot(lime_tag_x, tag_mpki)

plt.savefig('lime_tag_mpki.png')

fig9, ax = plt.subplots()
ax.set_xlabel("Signature Bits")
ax.set_ylabel("Normalized IPC")
ipc_ship_size = ax.plot(ship_size_x,ship_size_results)

plt.savefig('ship_size_ipc.png')

fig10, ax = plt.subplots()
ax.set_xlabel("Signature Bits")
ax.set_ylabel("Average MPKI")
mpki_ship_size = ax.plot(ship_size_x, ship_size_mpki)

plt.savefig('ship_size_mpki.png')


fig11, ax = plt.subplots()
ax.set_xlabel("Number of Trainers and History Size")
ax.set_ylabel("Normalized IPC")
ipc_lime_size = ax.plot(lime_size_x, lime_size_results)

plt.savefig('lime_size_ipc.png')

fig12, ax = plt.subplots()
ax.set_xlabel("Number of Trainers and History Size")
ax.set_ylabel("Average MPKI")
mpki_lime_size = ax.plot(lime_size_x, lime_size_mpki)

plt.savefig('lime_size_mpki.png')
plt.show()

