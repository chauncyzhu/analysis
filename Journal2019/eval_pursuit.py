# coding=utf8
"""
evaluation the results of pursuit game
"""
import matplotlib.pyplot as plt
import os
import numpy as np


eval_interval = 100
budget = 1800   # 2500 # 2147483647 # 1800
N=10
episode_num = 100

all_data_dir_name = "/home/cike/chauncy/game results/new pursuit game/data_2019_7_1_zhang's computer/"

all_data_dir = os.listdir(all_data_dir_name)
all_data_dir_list = []
for i in all_data_dir:
    now_dir_name = os.path.join(all_data_dir_name, i)
    if os.path.isdir(now_dir_name) and str(budget) in now_dir_name:
        for j in os.listdir(now_dir_name):
            all_data_dir_list.append(os.path.join(now_dir_name, j))

all_data_dir_list = sorted(all_data_dir_list)[::-1]


for i in all_data_dir_list:
    if "BasicQlearning" in i:
        file_name0 = i
        method_name0 = "Multi-IQL"
    
    if "AdhocTD" in i and "AdhocTDQSharing" not in i  and str(budget) in i:
        file_name1 = i
        method_name1 = "AdhocTD"
    
    if "AdhocTDQSharing" in i  and str(budget) in i:
        file_name2= i
        method_name2 = "AdhocTD-Q"
        
    if "PartakerSharerQSharing" in i and str(budget) in i:
        file_name3 = i
        method_name3 = "PSAF"



file_name_list = [file_name3, file_name1, file_name2, file_name0]
method_rank = [method_name3, method_name1, method_name2, method_name0]

  
def read_data(file_name_list):
    evaluation_data = []
    evaluation_budget = []

    for file_name in file_name_list:
        one_file_data = []
        one_file_budget = []
        with open(file_name, 'r') as f:
            for line in f.readlines():
                if ",," in line:
                    list_data = line.strip().split(",,")
                    data = []
                    budget = []
                    for j in list_data:
                        str_list = eval(j)
                        # print(str_list)
                        data.append(str_list[0])
                        budget.append((float(str_list[1]) + float(str_list[2]))/2)

                    one_file_data.append(data)
                    one_file_budget.append(budget)
            
        # evaluate the result each 100 interval
        def f(x):
            return [x[i:i+eval_interval] for i in range(len(x)) if i%eval_interval == 0]
        
        one_file_data = np.array((list(map(f, one_file_data)))).mean(axis=-1)
        one_file_budget = np.array((list(map(f, one_file_budget)))).mean(axis=-1)
        
        print(i.split("_")[1]+"_data shape:", np.array(one_file_data).shape)
        print(i.split("_")[1]+"_budget shape:", np.array(one_file_budget).shape)
        # use line data draw the pic
        evaluation_data.append(one_file_data.mean(axis=0)[:episode_num])
        evaluation_budget.append(one_file_budget.mean(axis=0)[:episode_num])

    return evaluation_data, evaluation_budget   
    

evaluation_datas, evaluation_budgets = read_data(file_name_list)                 
                    
                    
# image dir
save_fig_dir_name = "/home/cike/桌面/"

# save_fig_dir_name = all_data_dir_name

if not os.path.exists(save_fig_dir_name):
    os.mkdir(save_fig_dir_name)
                 
    
def plot_multi_TG(data_list, episodes, method_name_list, parameters, save=False):
    data_list = list(np.array(data_list)[:, :episodes])
    figure, ax = plt.subplots(figsize = figsize)
    for i, line in enumerate(data_list):
        plt.plot(range(len(line)), line, linewidth=parameters['linewidth'], 
            label=method_name_list[i], color=parameters['colors'][i], linestyle=parameters['linestyle'][i])

    plt.ylabel("Time to Goal", font2)
    plt.xlabel("x"+str(eval_interval)+" Traning Episodes", font2)
    if budget == 2147483647:
        plt.title("Four Predators Catch One Prey, b=+∞", font1)
    else:
        plt.title("Four Predators Catch One Prey, b="+str(budget), font1)
    
    plt.legend(loc='best', fontsize=annotate_size)
    
    # set tick
    if parameters['partPic']:
        plt.ylim(parameters['yMinMax'])
    
    plt.tick_params(labelsize=labelsize)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    if save:
        if parameters['partPic']:
            plt.savefig(save_fig_dir_name + "PP-TG-" + str(episodes)+"-"+str(budget)+"_nolegend_"+str(parameters['yMinMax'][1])+".eps", bbox_inches = 'tight', format="eps")
        else:
            plt.savefig(save_fig_dir_name + "PP-TG-" + str(episodes)+"-"+str(budget)+"_nolegend.eps", bbox_inches = 'tight', format="eps")

    plt.show()
    

def plot_multi_Budget(data_list, episodes, method_name_list, parameters, save=False):
    data_list = list(np.array(data_list)[:, :episodes])
    figure, ax = plt.subplots(figsize = figsize)
    for i, line in enumerate(data_list):
        plt.plot(range(len(line)), line, label=method_name_list[i], color=parameters['colors'][i], 
             linewidth=parameters['linewidth'], linestyle=parameters['linestyle'][i])
 
    plt.ylabel("Budget", font2)
    plt.xlabel("x"+str(eval_interval)+" Traning Episodes", font2)

    if budget == 2147483647:
        plt.title("Four Predators Catch One Prey, b=+∞", font1)
    else:
        plt.title("Four Predators Catch One Prey, b="+str(budget), font1)
    
    plt.legend(loc='best', fontsize=annotate_size)

    plt.tick_params(labelsize=labelsize)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    
    if save:
        plt.savefig(save_fig_dir_name + "PP-Budget-" + str(episodes)+"-"+str(budget)+"_short.eps", bbox_inches = 'tight', format="eps")

    plt.show()


font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 18,
         }
                    
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 20,
         }   
                 
figsize = 7, 5
labelsize = 18

plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300 


annotate_size = 18

parameters = {
    'legend_num': [1.02,0,3,0],
    "linestyle": ['-', ":", "-.", "--", ":", "-.", "--", ":", "-.", "--", ],
    "linewidth": 2,
    'colors': ['#7570b3', '#e7298a', '#66a61e', '#e6ab02', 'magenta', 'black'],
    'partPic': False,
    'yMinMax':[50, 200]
}


plot_multi_TG(evaluation_datas, episode_num, method_rank, parameters, True)


plot_multi_Budget(np.array(evaluation_budgets)[:-1, :], episode_num, method_rank[:-1], parameters, True)


