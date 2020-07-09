# -*- coding: utf-8 -*-
import numpy as np
import os
import matplotlib.pyplot as plt
from itertools import groupby
import pandas as pd

###########################################################
#################plot the changes of Q values##############
###########################################################
parameters = {
    'transparent':False,
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
    'colors': ['purple', 'yellow', 'pink', 'green', 'red', 'blue', 'orange', 'gray'],
    
    'scatter_s':35,
    'sc_marker': ['*', '1', "+", 'x', '>']

}
    
def plot_reuse_prob(data_list, point_list, action_list, parameters, save=False):
    figure, ax = plt.subplots(figsize = parameters['figsize'])
    for i, line in enumerate(data_list):
        plt.plot(range(len(line)), line, linewidth=parameters['linewidth'], label=parameters['label'][i], 
                 color=parameters['colors'][i], linestyle=parameters['linestyle'][i])

    
    for i in range(len(parameters['label'])):

        x = np.array(point_list[0])[np.array(action_list)[point_list[0].astype(int)]==i]
        y = np.array(point_list[1])[np.array(action_list)[point_list[0].astype(int)]==i]
        plt.scatter(list(x), list(y), c=parameters['colors'][i], marker=parameters['sc_marker'][i], s=parameters['scatter_s'],
                 label="Advised "+parameters['label'][i], linewidths=0, zorder=30)

    
    plt.ylabel("Q-values", parameters['font2'])
    plt.xlabel("traning step", parameters['font2'])
    plt.title("Predator-Prey domain", parameters['font1'])
    
    legend = plt.legend(bbox_to_anchor=(parameters['legend_num'][0], parameters['legend_num'][1]), fontsize=15.5, 
                               loc=parameters['legend_num'][2], borderaxespad=parameters['legend_num'][3])
    plt.tick_params(labelsize=parameters['tick_size'])
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    
    if parameters['transparent']:
        frame = legend.get_frame()
        frame.set_alpha(1)
        frame.set_facecolor('none') # 设置图例legend背景透明
    
    if save:
        plt.savefig(save_fig_dir_name + "Q-values.png", bbox_inches = 'tight')

    plt.show()
    
    
    
###########################################################
#################read the changes of Q values##############
###########################################################
dir_name = "/home/cike/chauncy/game results/action reuse/analyse/Q_changes/"
save_fig_dir_name = 'image/'

# key_words = "AdhocTDActionReuse_allQChanges"
key_words = "AdhocTD_allQChanges"


dir_files = os.listdir(dir_name)
data_list = []
data_map_agents = []
data_index_map_agents = []

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
    data_index_map = {}
    for line in agent:   # each state
        key = line.split(":")[0]
        try:
            value = line.split(":")[1]
            value = value.split("|")
            # store the index of episode and step 
            state_list = []
            info_list = []
            for va in value:
                va_list = va.split(",,")[:-1]
                new_va_list = [list(i.split(",")) for i in va_list]
                state_list.append(new_va_list)

                info_list.append(va.split(",,")[-1].split(","))   
            data_map[key] = state_list
            data_index_map[key] = info_list            
        except:
            print("wrong:",line)
            raise(Exception("wrong")) 
    data_map_agents.append(data_map)
    data_index_map_agents.append(data_index_map)              


####################find a key containing many actions###############    
agent_num = 0
agent1_data = data_map_agents[agent_num]
agent1_index_data = data_index_map_agents[agent_num]
len_map = {}
for key in agent1_data.keys():
    info = np.array(agent1_index_data[key], dtype=np.int32).T[0]
    len_map[key] = len(info[info>-1])
    
    info_series = pd.Series(info)
    len_map[key] = len(info_series.unique())
    
count = 0
for key in len_map.keys():
    count+=len_map[key]
print(count)
    

############################ prepare data############################    
state_key = "2,0,2,1"

# find a certain state
state_list = agent1_data[state_key]
info_list = agent1_index_data[state_key]
state_list = np.array(state_list, dtype=np.float32)
info_list = np.array(info_list, dtype=np.int32)

agent1_values = state_list[:, 0, :].T
agent1_peer_values = state_list[:, 1, :].T   # peer's Q values in agent1's state
agent1_peer_state_values = state_list[:, 2, :].T   # peer's Q values in agent1's state
agent1_advised = info_list.T
                          
# prepare the point
agent1_advised_point = []
agent1_advised_action = agent1_advised[0]
for index, value in enumerate(agent1_advised_action):
    if value != -1:
        agent1_advised_point.append([index, agent1_values[value][index]])  

agent1_advised_point = list(np.array(agent1_advised_point).T)


############################ plot the Q-values of agent1###############    
plt.rcParams['savefig.dpi'] = 100
plt.rcParams['figure.dpi'] = 100 

plot_reuse_prob(agent1_values, agent1_advised_point, agent1_advised_action, parameters, True)