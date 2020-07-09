# coding=utf8

import os

import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

# dir_name = "/home/cike/IdeaProjects/Mario/data/teacherS/independent"
total_dir = "/home/cike/IdeaProjects/Mario/data/teacherS"

dir_name_one = total_dir + "/independent_res"

# read files from directory
name_list = [total_dir + "/independent_policy"]
label_list = ["IL-Q(λ)"]
data_dir_path = "/data_ask_2_give_0.2_ep_0" # "/data_ask_2_give_0.2_ep_0" 

dir_list = os.listdir(total_dir + data_dir_path)
dir_list.sort(reverse=True)
for i in dir_list:
    if "figure" not in i:
        if i.startswith("adhoctd"):
            label_list.append("AdhocTD")
            name_list.append(os.path.join(total_dir + data_dir_path, i))

        if i.startswith("change") and "0.0_" in i:
            label_list.append("AdhocTD-QChange-0") 
            name_list.append(os.path.join(total_dir + data_dir_path, i))

        if i.startswith("change") and "0.001_" in i:
            label_list.append("AdhocTD-QChange-0.001") 
            name_list.append(os.path.join(total_dir + data_dir_path, i))
        
        if i.startswith("change") and "0.01_" in i:
            label_list.append("AdhocTD-QChange-0.01") 
            name_list.append(os.path.join(total_dir + data_dir_path, i))
        
        if i.startswith("change") and "0.02" in i:
            label_list.append("AdhocTD-QChange-0.02") 
            name_list.append(os.path.join(total_dir + data_dir_path, i))
        
        if i.startswith("change") and "0.03" in i:
            label_list.append("AdhocTD-QChange-0.03") 
            name_list.append(os.path.join(total_dir + data_dir_path, i))

        if i.startswith("decay") and "0.99_" in i:
            label_list.append("AdhocTD-Decay-0.99")
            name_list.append(os.path.join(total_dir + data_dir_path, i))

        if i.startswith("decay") and '0.9_' in i:
            label_list.append("AdhocTD-Decay-0.9")
            name_list.append(os.path.join(total_dir + data_dir_path, i))

        if i.startswith("decay") and '0.8_' in i:
            label_list.append("AdhocTD-Decay-0.8")
            name_list.append(os.path.join(total_dir + data_dir_path, i))

        if i.startswith("budget") and '5_' in i:
            label_list.append("AdhocTD-Budget-5")
            name_list.append(os.path.join(total_dir + data_dir_path, i))

        if i.startswith("budget") and '10_' in i:
            label_list.append("AdhocTD-Budget-10")
            name_list.append(os.path.join(total_dir + data_dir_path, i))

        if i.startswith("budget") and '100_' in i:
            label_list.append("AdhocTD-Budget-100")
            name_list.append(os.path.join(total_dir + data_dir_path, i))


def getData(dir_name_list):
    dir_data_list = []
    for dir_name in dir_name_list:
        dir_file_names = os.listdir(dir_name)
        data_list = []
        for i in dir_file_names:
            if "score" in i:  # print(i)
                one = open(os.path.join(dir_name, i), "r")
                lines = one.readlines()
                data = []
                for line in lines:
                    line = line.strip().split(",")
                    data.append([float(line[i]) for i in range(len(line))])

                data_list.append(data)
        dir_data_list.append(data_list)
    return dir_data_list

interval = 100
def parse_data(data_final):
    first_data = data_final[0]
    # last_data = data_final[-1]

    data_final = data_final[1:]
    y_data = [np.mean(data_final[i:i+interval]) for i in range(len(data_final)) if i % interval == 0]
    y_data = [first_data] + y_data # + [last_data]
    # print(y_data[-1])
    return y_data
# print(y_data)

def get_episode_reward(data):
    # print(data)
    episode_reward = np.mean(data, axis=0)[:, 1]
    final = parse_data(episode_reward)
    return list(final)

def get_budget(data):
    budget = np.mean(data, axis=0)[:, -1]
    final = parse_data(budget)
    return list(final)


def list_dict(keys, values):
    dict_data = {}
    assert isinstance(keys, list) and isinstance(values, list)
    if len(keys) != len(values):
        return
    for index, key in enumerate(keys):
        dict_data[key] = values[index]
    return dict_data

##############################################read data########################################
##############################################read data########################################
##############################################read data########################################
dir_data_list = getData(name_list)
y_reward_list = [get_episode_reward(i) for i in dir_data_list]
y_budget_list = [get_budget(i) for i in dir_data_list]


for i, y_data in enumerate(y_reward_list):
    print("Method:"+label_list[i], "|Initial REWARD:", round(y_data[0], 3), "|LAST REWARD:", round(y_data[-1], 3), 
          "|AVG REWARD:", round(np.mean(y_data), 3))


for i, y_data in enumerate(y_reward_list):
    print("Method:"+label_list[i], str(round(y_data[0], 3))+"&"+str(round(y_data[-1], 3))+"&"+str(round(np.mean(y_data), 3)))


##############################################read data########################################
##############################################read data########################################
##############################################read data########################################


font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 18,
         }

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 20,
         }

plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300
parameters = {
    'figsize': (6, 5),
    'labelsize': 18,
    'annotate_size': 15,
    'save_pic': True,
    'save_path': total_dir + data_dir_path + "/figures_ep_0",
    'legend_num': [1.02, 0, 3, 0],
    "linestyle": ['-', "-.", ":", "--", '-'],
    "linewidth": [3,1.5,1.5,1.5,1.5],
}

colors = ['grey', 'Orange', 'Green', 'DodgerBlue', 'PeachPuff', 'Turquoise', 'pink', 'Brown', 'DeepPink']


def plt_data(y_list, label_list, jump, parameters, text, comments):
    figure, ax = plt.subplots(figsize=parameters['figsize'])
    for i, y_data in enumerate(y_list):
        if i not in jump:
            plt.plot(range(len(y_data)), y_data, label=label_list[i], c=parameters['colors'][i],
                     linewidth=parameters['linewidth'][i], linestyle=parameters['linestyle'][i])

    plt.xlabel(text['xlabel'], font2)
    plt.ylabel(text['ylabel'], font2)
    plt.title(text['title'], font2)
    
    # new_ticks = np.linspace(0,1,500)
    # plt.xticks(new_ticks)
    
    plt.legend(loc='best', fontsize=parameters['annotate_size'])
    plt.tick_params(labelsize=parameters['labelsize'])
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    

    if parameters['save_pic']:
        if not os.path.exists(parameters['save_path']):
            os.mkdir(parameters['save_path'])
        plt.savefig(parameters['save_path'] + "/" + comments, bbox_inches = 'tight')
    plt.show()



text_reward = {
    "xlabel": "x100 Traning Episodes",
    "ylabel": "Average Reward",
    "title": "The ARE in Mario"
}

text_budget = {
    "xlabel": "x100 Traning Episodes",
    "ylabel": "Budget",
    "title": "The Consumed Budget in Mario"
}

#index = [0, 3, (len(y_reward_list)-1)]

print(label_list)
# prepare data
reward_data_map = list_dict(label_list, y_reward_list)
budget_data_map = list_dict(label_list, y_budget_list)

############################################################
######################## Three methods compare #############
label_new =['IL-Q(λ)', 'AdhocTD', 'AdhocTD-QChange-0', 'AdhocTD-Budget-5', 'AdhocTD-Decay-0.9']
parameters['colors'] = ['Grey', 'Gold', 'LimeGreen', 'OrangeRed', 'MediumPurple']

y_reward_new = itemgetter(*label_new)(reward_data_map)
y_budget_new = itemgetter(*label_new)(budget_data_map)

jump = []
plt_data(y_reward_new, label_new, jump, parameters, text_reward, 'ARE_methods_compare_mario')

jump = [0]
plt_data(y_budget_new, label_new, jump, parameters, text_budget, 'Budget_methods_compare_mario')
######################## Three methods compare #############
############################################################






