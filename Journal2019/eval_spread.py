#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:38:56 2019

@author: cike
"""
# eval spread domain
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



budget = 1500   # 1500
episode_num = 500

if budget == "inf":
    all_data_dir_name = "/home/cike/chauncy/game results/spread_domain/unlimited_new_20190622/"

if budget == 3000:
    all_data_dir_name = "/home/cike/chauncy/game results/spread_domain/3000_new_20190630/"

if budget == 1500:
    all_data_dir_name = "/home/cike/chauncy/game results/spread_domain/1500_20200122"



all_data_dir = os.listdir(all_data_dir_name)
all_data_dir_list = []
for i in all_data_dir:
    now_dir_name = os.path.join(all_data_dir_name, i)
    if os.path.isdir(now_dir_name):
        all_data_dir_list.append(now_dir_name)

all_data_dir_list = sorted(all_data_dir_list)[::-1]


for i in all_data_dir_list:
    if "QLearner" in i:
        file_name1 = i
        method_name1 = "Multi-IQL"
    if "AdhocTD" in i and "AdhocTDQ" not in i:
        file_name2 = i
        method_name2 = "AdhocTD"
    if "AdhocTDQ" in i:
        file_name3 = i
        method_name3 = "AdhocTD-Q"
    if "PartakerSharerTD" in i:
        file_name4 = i
        method_name4 = "PSAF"


file_name_list = [file_name4, file_name2, file_name3, file_name1]
method_rank = [method_name4, method_name2, method_name3, method_name1]

columns_name = []
all_data = []
for fnl in file_name_list:
    np_data_final = []
    dir_name = os.path.join(fnl, "Evaluations")
    for file_name in os.listdir(dir_name):
        pd_data = pd.read_csv(os.path.join(dir_name, file_name))
        np_data = np.array(pd_data)
        columns_name = list(pd_data.columns)
        np_data_final.append(np_data)
    
    all_data.append(np.mean(np_data_final, axis=0))
    
print("data shape:", np.shape(all_data))        
        

font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 18,
         }
                    
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 20,
         }   
                 
figsize = 6, 5
labelsize = 18

plt.rcParams['savefig.dpi'] = 150
plt.rcParams['figure.dpi'] = 150 


annotate_size = 18

parameters = {
    'legend_num': [1.02,0,3,0],
    "linestyle": ['-', ":", "-.", "--", ":", "-.", "--", ":", "-.", "--", ],
    "linewidth": 2,
    'colors': ['#7570b3', '#e7298a', '#66a61e', '#e6ab02', 'magenta', 'black']
}
    

save_fig_dir_name = "/home/cike/桌面/"
save_fig_dir_name = all_data_dir_name + "/"

def plot_avg_reward(data_list, episodes, method_name_list, ylabel, title, parameters, save=False):
    data_list = list(np.array(data_list)[:, :episodes])
    figure, ax = plt.subplots(figsize = figsize)
    for i, line in enumerate(data_list):
        plt.plot(range(len(line)), line, linewidth=parameters['linewidth'], 
            label=method_name_list[i], color=parameters['colors'][i], linestyle=parameters['linestyle'][i])

    plt.ylabel(ylabel, font2)
    plt.xlabel("x100 Traning Episodes", font2)
    if budget == 'inf':
        plt.title(title + ", b=+∞", font1)
    else:
        plt.title(title + ", b="+str(budget), font1)
    
    # plt.legend(bbox_to_anchor=(parameters['legend_num'][0], parameters['legend_num'][1]), fontsize=15.5, 
                               # loc=parameters['legend_num'][2], borderaxespad=parameters['legend_num'][3])
    
    
    plt.legend(loc='best', fontsize=annotate_size)
    
    plt.tick_params(labelsize=labelsize)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    if save:
        ylabel = "-".join(ylabel.split(" "))
        plt.savefig(save_fig_dir_name + "Spread-"+ylabel+"-" + str(episodes)+"-"+str(budget)+".eps", bbox_inches = 'tight', format="eps")

    plt.show()
        
ylabel = ['Budget', 'Average reward per step', 'Auc score']
title = 'Two agents cover two landmarks'


all_data = np.array(all_data)

plot_avg_reward(np.mean(all_data[:, :, 1:3], axis=-1)[:3, :], episode_num, method_rank, ylabel[0], title, parameters, True)
plot_avg_reward(all_data[:, :, 3], episode_num, method_rank, ylabel[1], title, parameters, True)
plot_avg_reward(all_data[:, :, 4], episode_num, method_rank, ylabel[2], title, parameters, True)




