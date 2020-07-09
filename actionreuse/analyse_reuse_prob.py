# -*- coding: utf-8 -*-
import numpy as np
import os
import matplotlib.pyplot as plt
from itertools import groupby


###########################################################
#################plot the changes of action prob###########
###########################################################
def plot_reuse_prob(data_list, parameters, save=False):
    figure, ax = plt.subplots(figsize = parameters['figsize'])
    for i, line in enumerate(data_list):
        plt.plot(range(len(line)), line, linewidth=parameters['linewidth'], label=parameters['label'][i], 
                 color=parameters['colors'][i], linestyle=parameters['linestyle'][i])

    plt.ylabel("reusing probability", parameters['font2'])
    plt.xlabel("traning step", parameters['font2'])
    plt.title("Predator-Prey domain", parameters['font1'])
    
    plt.legend(bbox_to_anchor=(parameters['legend_num'][0], parameters['legend_num'][1]), fontsize=15.5, 
                               loc=parameters['legend_num'][2], borderaxespad=parameters['legend_num'][3])
    plt.tick_params(labelsize=parameters['tick_size'])
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    if save:
        plt.savefig(save_fig_dir_name + "reuse-prob.png", bbox_inches = 'tight')

    plt.show()

parameters = {
    'font1': {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 14,
         },
                    
    'font2': {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 22,
         },
    'figsize': (6, 5),
    'tick_size': 14, 
    'label': ["UP", "DOWN", "LEFT", "RIGHT", "STAY"],
    'legend_num': [1.02,0,3,0],
    "linestyle": ['-', ":", "-.", "--", ":", "-.", "--", ":", "-.", "--", ],
    "linewidth": 2,
    'colors':['#7570b3', '#e7298a', '#66a61e', '#e6ab02', 'magenta', 'black']

}

###########################################################
#################read the changes of action prob###########
###########################################################
dir_name = "/home/cike/chauncy/game results/action reuse/analyse/Prob_changes/"
save_fig_dir_name = 'image/'

key_words = "AdhocTDActionReuse_allProbChanges"

dir_files = os.listdir(dir_name)
data_list = []
data_map_agents = []

agent_data_list = []
for i in dir_files:
    if key_words in i:
        file_path = os.path.join(dir_name, i)
        data_list = open(file_path, 'rb')
        data_list = data_list.readlines()
        data_list = list(map(lambda x:x.decode().strip(), data_list))
        
data_list = [list(group) for k, group in groupby(data_list, lambda x:x=="agent") if not k]
for agent in data_list:
    data_map = {}
    for line in agent:   # each state
        key = line.split(":")[0]
        try:
            value = line.split(":")[1]
            value = value.split("|")
            value = list(map(lambda x:x.split(","), value))
            data_map[key] = value
        except:
            print("wrong:",line)
            raise(Exception("wrong")) 
    data_map_agents.append(data_map)




# find a certain state
agent_num = 0
agent1_data = data_map_agents[agent_num]
len_map = {}

for key in agent1_data.keys():
    data = np.array(agent1_data[key], dtype=np.float32) 
    data = data.mean(axis=0)
    len_map[key] = len(data[data>0])

count = 0
for key in len_map.keys():
    count+=len_map[key]
    if (len_map[key]>2):
        print(key)
print(count)
    


state_key = "-2,2,-2,1"
state_list = data_map_agents[0][state_key]

state_list = np.array(state_list, dtype=np.float32).T

plt.rcParams['savefig.dpi'] = 100
plt.rcParams['figure.dpi'] = 100 

plot_reuse_prob(state_list, parameters, True)





