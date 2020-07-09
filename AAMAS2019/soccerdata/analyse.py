# -*- coding: utf-8 -*-

"""
analyse changes of Q values, and the max Q's action
"""
import os
import pickle as pkl

temp_dir = {}
dir_path = "soccerdata/actionvisit_20180507/"
dir_files = os.listdir(dir_path)
for i in dir_files:
    if "AGENT_2" in i and "action" in i:
        file_path = os.path.join(dir_path, i)
        my_file = pkl.load(open(file_path, "rb"))

        # print(file_path)
        
        for keys in my_file:
            # print(keys, my_file[keys])
            if keys[0] not in temp_dir:
                temp_dir[keys[0]] = {keys[1]:my_file[keys]}
            else:
                temp_dir[keys[0]][keys[1]] = my_file[keys]


all_kyes = []
len_keys = []
for keys in my_file:
    all_kyes.append(keys)
    len_keys.append(len(my_file[keys]))


import numpy as np
max_keys = all_kyes[np.argmax(len_keys)]
len(temp_dir[max_keys[0]])


all_kyes_temp = []
len_keys_temp = []
for keys in temp_dir:
    if len(temp_dir[keys]) > 3:
        all_kyes_temp.append(keys)
        len_keys_temp.append(sum([len(temp_dir[keys][i]) for i in temp_dir[keys]]))

max_len_keys = all_kyes_temp[np.argmax(len_keys_temp)]
max_len_keys_values = temp_dir[max_len_keys]


import matplotlib.pyplot as plt
max_len = max([len(max_len_keys_values[i]) for i in max_len_keys_values])
# max_len = 30000
plt.figure()
for i in max_len_keys_values:
    if max_len > len(max_len_keys_values[i]):
        plt.plot(range(max_len), max_len_keys_values[i]+[max_len_keys_values[i][-1]]*(max_len-len(max_len_keys_values[i])))
    else:
        plt.plot(range(max_len), max_len_keys_values[i][:max_len])

plt.show()
    
    

# agent 1
# max_len_keys_agent1 = max_len_keys
# max_len_keys_values_agents = max_len_keys_values

    
max_len_keys_agent2 = max_len_keys
max_len_keys_values_agent2 = max_len_keys_values    
    
    
agent1_in_agent2 = temp_dir[max_len_keys_agent1]    
    
import matplotlib.pyplot as plt
max_len = max([len(agent1_in_agent2[i]) for i in agent1_in_agent2])
# max_len = 30000
plt.figure()
for i in agent1_in_agent2:
    if max_len > len(agent1_in_agent2[i]):
        plt.plot(range(max_len), agent1_in_agent2[i]+[max_len_keys_values[i][-1]]*(max_len-len(agent1_in_agent2[i])))
    else:
        plt.plot(range(max_len), agent1_in_agent2[i][:max_len])

plt.show()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    