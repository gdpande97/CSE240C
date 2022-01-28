import os
from scipy.stats import gmean
import matplotlib.pyplot as plt

results_dir = ['results_FNL3MMA7','results_FNL3MMA9','results_FNL3MMA12','results_FNL3MMA25']

os.chdir('./results')

gmean_arr = []

ipc_gmean_map = {}
ipc_map = {}

count = 0
for folder in os.listdir():
    
    os.chdir(folder)
    start = folder.find('results_')
    result_arr = []
    folder_name =  folder[8:]
    for result in os.listdir():
        file1 = open(result, 'r')
        lines = file1.readlines()
        
        for line in lines:
            if line.find('Finished') != -1:
                start = int(line.find('IPC:'))
                end = int(line.find('(Simulation'))
                ipc_val = float(line[start+4: end])
                result_arr.append(float(ipc_val))
            # if line.find('')
    ipc_map[folder_name] = result_arr    
    gmean_val = gmean(result_arr)
    ipc_gmean_map[folder_name] = gmean_val
    os.chdir('./..')

#For reproducing results

for key in ipc_gmean_map:
    print(key + ": " + str(ipc_gmean_map[key]))

original_result_keys= ['baseline', 'barca_normal', 'FNLMMA']
original_results = []
for x in original_result_keys:
    normalized_val = ((ipc_gmean_map[x]/ipc_gmean_map['baseline']) - 1) * 100
    formatted_val = "{:.7f}".format(normalized_val)
    original_results.append(float(formatted_val))

original_graph_keys = ['Baseline', 'BARCA', 'FNLMMA']

#barca design space exploration:
barca_de1_keys = ['barca_3', 'barca_4', 'barca_30', 'barca_6', 'barca_7' ]
barca_de1_graph =['3', '4', '5', '6' ,'7']
barca_de2_keys = ['barca_4_r', 'barca_30', 'barca_6_r', 'barca_7_r', 'barca_8_r', 'barca_9_r']
barca_de2_graph = ['4', '5', '6', '7', '8', '9']
barca_de1_results = []
barca_de2_results = []

for x in barca_de1_keys:
    normalized_val = ((ipc_gmean_map[x]/ipc_gmean_map['baseline_30']) - 1) * 100
    formatted_val = "{:.7f}".format(normalized_val)
    barca_de1_results.append(float(formatted_val))

for x in barca_de2_keys:
    normalized_val = ((ipc_gmean_map[x]/ipc_gmean_map['baseline_30']) - 1) * 100
    formatted_val = "{:.5f}".format(normalized_val)
    barca_de2_results.append(float(formatted_val))



#FNLMMA design space exploration:
fnlmma_de1_keys = ['FNL3MMA7', 'FNL3MMA9', 'FNL3MMA12', 'FNL3MMA25', 'FNL5MMA7', 'FNL5MMA9', 'FNLMMA_30', 'FNL5MMA12', 'FNL5MMA15', 'FNL5MMA25']
fnlmma_de1_graph = ['3,7', '3,9', '3,12', '3,25', '5,7', '5,9', '5,10', '5,12', '5,15', '5,25']
fnlmma_de2_keys = ['FNLMMA_4096', 'FNLMMA_30', 'FNLMMA_12288', 'FNLMMA_16384']
fnlmma_de2_graph = ['4096', '8192', '12288', '16384']

fnlmma_de1_results = []
fnlmma_de2_results = []

for x in fnlmma_de1_keys:
    normalized_val = ((ipc_gmean_map[x]/ipc_gmean_map['baseline_30']) - 1) * 100
    formatted_val = "{:.2f}".format(normalized_val)
    fnlmma_de1_results.append(float(formatted_val))

for x in fnlmma_de2_keys:
    normalized_val = ((ipc_gmean_map[x]/ipc_gmean_map['baseline_30']) - 1) * 100
    formatted_val = "{:.7f}".format(normalized_val)
    fnlmma_de2_results.append(float(formatted_val))

barca_scale_keys = ['barca_8sets', 'barca_32sets', 'barca_128sets', 'barca_30', 'barca_512sets', 'barca_2048sets']
barca_scale_graph = ['8', '32', '128', '256', '512', '2048']
fnlmma_scale_keys = ['FNLMMA_oneeighth', 'FNLMMA_onefourth', 'FNLMMA_half', 'FNLMMA_30', 'FNLMMA_twice', 'FNLMMA_quadruple', 'FNLMMA_eighttimes']
fnlmma_scale_graph = ['1/8', '1/4', '1/2', '1', '2', '4', '8']
barca_scale_results = []
fnlmma_scale_results = []

for x in barca_scale_keys:
    normalized_val = ((ipc_gmean_map[x]/ipc_gmean_map['baseline_30']) - 1) * 100
    formatted_val = "{:.6f}".format(normalized_val)
    barca_scale_results.append(float(formatted_val))

for x in fnlmma_scale_keys:
    normalized_val = ((ipc_gmean_map[x]/ipc_gmean_map['baseline_30']) - 1) * 100
    formatted_val = "{:.5f}".format(normalized_val)
    fnlmma_scale_results.append(float(formatted_val))


fig1, ax  = plt.subplots()

rep_res = ax.bar(original_graph_keys, original_results)
for r in rep_res:
   height = r.get_height()
   ax.annotate('{}'.format(height),
      xy=(r.get_x() + r.get_width() / 2, height),
      xytext=(0, 3), # 3 points vertical offset
      textcoords="offset points",
      ha='center', va='bottom')
plt.xlabel('Prefetchers')
plt.ylabel('Performance improvement in %')
plt.title('Results of Barca and FNLMMA')

plt.savefig('reproduced_results.png')
# plt.show()


fig2, ax = plt.subplots()
barca_de1 = ax.bar(barca_de1_graph, barca_de1_results)
for r in barca_de1:
    height = r.get_height()
    ax.annotate('{}'.format(height),
      xy=(r.get_x() + r.get_width() / 2, height),
      xytext=(0, 3), # 3 points vertical offset
      textcoords="offset points",
      ha='center', va='bottom')
plt.xlabel('Search Depth')
plt.ylabel('Performance improvement in %')
plt.title('Results of Barca Search Depth')

plt.savefig('barca_depth.png')

fig3, ax = plt.subplots()
barca_de2 = ax.bar(barca_de2_graph, barca_de2_results)
for r in barca_de2:
    height = r.get_height()
    ax.annotate('{}'.format(height),
      xy=(r.get_x() + r.get_width() / 2, height),
      xytext=(0, 3), # 3 points vertical offset
      textcoords="offset points",
      ha='center', va='bottom')
plt.xlabel('Recency Queue Length')
plt.ylabel('Performance improvement in %')
plt.title('Results of varying Recency Queue length in Barca')

plt.savefig('barca_recency.png')

fig4, ax = plt.subplots()
fnlmma_de1 = ax.bar(fnlmma_de1_graph, fnlmma_de1_results)
for r in fnlmma_de1:
    height = r.get_height()
    ax.annotate('{}'.format(height),
      xy=(r.get_x() + r.get_width() / 2, height),
      xytext=(0, 3), # 3 points vertical offset
      textcoords="offset points",
      ha='center', va='bottom')
plt.xlabel('Changes in FNL length and MMA lookahead')
plt.ylabel('Performance improvement in %')
plt.title('Results of varying FNL Length and MMA Lookahead distance in FNLMMA')

plt.savefig('fnlmma_length.png')

fig5, ax = plt.subplots()
fnlmma_de2 = ax.bar(fnlmma_de2_graph, fnlmma_de2_results)
for r in fnlmma_de2:
    height = r.get_height()
    ax.annotate('{}'.format(height),
      xy=(r.get_x() + r.get_width() / 2, height),
      xytext=(0, 3), # 3 points vertical offset
      textcoords="offset points",
      ha='center', va='bottom')
plt.xlabel('Changes in reset period')
plt.ylabel('Performance improvement in %')
plt.title('Results of varying reset period in FNLMMA')

plt.savefig('fnlmma_reset.png')

fig6, ax = plt.subplots()
barca_scale = ax.bar(barca_scale_graph, barca_scale_results)
for r in barca_scale:
    height = r.get_height()
    ax.annotate('{}'.format(height),
      xy=(r.get_x() + r.get_width() / 2, height),
      xytext=(0, 3), # 3 points vertical offset
      textcoords="offset points",
      ha='center', va='bottom')
plt.xlabel('Number of sets in the prefetcher')
plt.ylabel('Performance improvement in %')
plt.title('Results of varying sizes in BARCA')

plt.savefig('barca_scale.png')

fig7, ax = plt.subplots()
fnlmma_scale = ax.bar(fnlmma_scale_graph, fnlmma_scale_results)
for r in fnlmma_scale:
    height = r.get_height()
    ax.annotate('{}'.format(height),
      xy=(r.get_x() + r.get_width() / 2, height),
      xytext=(0, 3), # 3 points vertical offset
      textcoords="offset points",
      ha='center', va='bottom')
plt.xlabel('Multiplying factor with original size')
plt.ylabel('Performance improvement in %')
plt.title('Results of varying sizes in FNLMMA')

plt.savefig('fnlmma_scale.png')

plt.show()
