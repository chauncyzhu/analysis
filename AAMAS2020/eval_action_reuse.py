# coding=utf8
"""
evaluation the results of pursuit game
"""
import matplotlib.pyplot as plt
import os
import numpy as np


def list_all_dir_name(dir_name):
    data_dir = os.listdir(dir_name)
    data_dir_list = []
    for i in data_dir:
        now_dir_name = os.path.join(dir_name, i)
        if os.path.isdir(now_dir_name):
            for j in os.listdir(now_dir_name):
                data_dir_list.append(os.path.join(now_dir_name, j))
    
    data_dir_list = sorted(data_dir_list)[::-1]
    return data_dir_list


def read_data(file_names, method_names):
    evaluation_data = {}
    evaluation_budget = {}

    for index, file_name in enumerate(file_names):
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
        
        print(method_names[index], "data:", np.array(one_file_data).shape, "budget:", np.array(one_file_budget).shape)
        # use line data draw the pic
        evaluation_data[method_names[index]] = one_file_data.mean(axis=0)
        evaluation_budget[method_names[index]] = one_file_budget.mean(axis=0)

    return evaluation_data, evaluation_budget   
    
# align data
def align_data(data, length):
    new_data = {}
    for key in data.keys():
        new_data[key] = data[key][:length]
    return new_data



    
def plot_multi_TG(data_list, episodes, method_name_list, parameters, save=False):
    data_list = list([data[:episodes] for data in data_list])
    figure, ax = plt.subplots(figsize = figsize)
    for i, line in enumerate(data_list):
        plt.plot(range(len(line)), line, linewidth=parameters['linewidth'], 
            label=method_name_list[i], color=parameters['colors'][i], linestyle=parameters['linestyle'][i])

    plt.ylabel("Time to Goal", parameters['label_font'])
    plt.xlabel("x"+str(eval_interval)+" Traning Episodes", parameters['label_font'])
    if budget > 10000:
        plt.title("The TG in PP Domain", parameters['title_font'])
    else:
        plt.title(parameters['title']+", b="+str(budget), parameters['title_font'])
    
    # plt.legend(bbox_to_anchor=(parameters['legend_num'][0], parameters['legend_num'][1]), fontsize=15.5, 
                               # loc=parameters['legend_num'][2], borderaxespad=parameters['legend_num'][3])
    
    if parameters['partPic']:
        plt.ylim(parameters['yMinMax'])
        
    plt.legend(loc='best', fontsize=parameters['legend_font'])
    
    plt.tick_params(labelsize=labelsize)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    if save:
        if not parameters['partPic']:
            if budget > 10000:
                plt.savefig(save_fig_dir_name + "PP-"+parameters['save_name']+"TG-" + str(episodes)+"-inf.png", bbox_inches = 'tight')
            else:
                plt.savefig(save_fig_dir_name + "PP-"+parameters['save_name']+"TG-" + str(episodes)+"-"+str(budget)+".png", bbox_inches = 'tight')
        else:
            if budget > 10000:
                plt.savefig(save_fig_dir_name + "PP-"+parameters['save_name']+"TG-" + str(episodes)+"-inf-part.png", bbox_inches = 'tight')
            else:
                plt.savefig(save_fig_dir_name + "PP-"+parameters['save_name']+"TG-" + str(episodes)+"-"+str(budget)+"-part.png", bbox_inches = 'tight')

    plt.show()
    

def plot_multi_Budget(data_list, episodes, method_name_list, parameters, save=False):
    data_list = list([data[:episodes] for data in data_list])
    figure, ax = plt.subplots(figsize = figsize)
    for i, line in enumerate(data_list):
        plt.plot(range(len(line)), line, label=method_name_list[i], color=parameters['colors'][i], 
             linewidth=parameters['linewidth'], linestyle=parameters['linestyle'][i])
 
    plt.ylabel("Budget", parameters['label_font'])
    plt.xlabel("x"+str(eval_interval)+" Traning Episodes", parameters['label_font'])

    if budget > 10000:
        plt.title("The Consumed Budget in PP Domain", parameters['title_font'])
    else:
        plt.title("Four Predators Catch One Prey, b="+str(budget), parameters['title_font'])
    
    # plt.legend(bbox_to_anchor=(parameters['legend_num'][0], parameters['legend_num'][1]), fontsize=15.5, 
      #                         loc=parameters['legend_num'][2], borderaxespad=parameters['legend_num'][3])
    
    plt.legend(loc='best', fontsize=parameters['legend_font'])

    plt.tick_params(labelsize=labelsize)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    
    if save:
        if budget > 10000:
            plt.savefig(save_fig_dir_name + "PP-"+parameters['save_name']+"Budget-" + str(episodes)+"-inf.png", bbox_inches = 'tight')
        else:
            plt.savefig(save_fig_dir_name + "PP-"+parameters['save_name']+"Budget-" + str(episodes)+"-"+str(budget)+".png", bbox_inches = 'tight')

    plt.show()
    
    
    
eval_interval = 100
budget = 2147483647 # 3000 # 2147483647  # 3000 # 2147483647
N=10

dir_name_one = "/home/cike/chauncy/game results/new action reuse/data_20190703/"
dir_name_two = "/home/cike/chauncy/game results/new action reuse/new q change_20190713/"

decay_dir_list = list_all_dir_name(dir_name_one) 

var_length = 24
for i in range(var_length):
    locals()["file_name"+str(i)] = None
    locals()["method_name"+str(i)] = None
    

for i in decay_dir_list:        
    if "AdhocTDActionReuseDecay" in i and "-0.999 decay" in i:
        file_name0 = i
        method_name0 = "Decay-0.999"
        
    if "AdhocTDActionReuseDecay" in i and "-0.99 decay" in i:
        file_name1 = i
        method_name1 = "Decay-0.99"
    
    if "AdhocTDActionReuseDecay" in i and "-0.95 decay" in i:
        file_name2 = i
        method_name2 = "Decay-0.95"
        
    if "AdhocTDActionReuseDecay" in i and "-0.9 decay" in i:
        file_name3 = i
        method_name3 = "Decay-0.9"
        
    if "AdhocTDActionReuseDecay" in i and "-0.8 decay" in i:
        file_name4 = i
        method_name4 = "Decay-0.8"



    if "AdhocTDActionReuseQChange" in i and "-0.0 thre" in i:
        file_name5 = i
        method_name5 = "QChange-0"
        
    if "AdhocTDActionReuseQChange" in i and "-0.01 thre" in i:
        file_name6 = i
        method_name6 = "QChange-0.01"
        
    if "AdhocTDActionReuseQChange" in i and "-0.02 thre" in i:
        file_name7 = i
        method_name7 = "QChange-0.02"    
    
    if "AdhocTDActionReuseQChange" in i and "-0.03 thre" in i:
        file_name8 = i
        method_name8 = "QChange-0.03"
    
    if "AdhocTDActionReuseQChange" in i and "-0.04 thre" in i:
        file_name8 = i
        method_name8 = "QChange-0.04"
        
    if "AdhocTDActionReuseQChange" in i and "-0.05 thre" in i:
        file_name10 = i
        method_name10 = "QChange-0.05"



    if "AdhocTDActionReuseFixedLength" in i and "-5 len" in i:
        file_name11 = i
        method_name11 = "FixedLength-5"

    if "AdhocTDActionReuseFixedLength" in i and "-20 len" in i:
        file_name12 = i
        method_name12 = "FixedLength-20"
        
    if "AdhocTDActionReuseFixedLength" in i and "-50 len" in i:
        file_name13 = i
        method_name13 = "FixedLength-50"
        
    if "AdhocTDActionReuseFixedLength" in i and "-100 len" in i:
        file_name14 = i
        method_name14 = "FixedLength-100"
  
    if "AdhocTDActionReuseFixedLength" in i and "-150 len" in i:
        file_name15 = i
        method_name15 = "FixedLength-150"
        
        
comparing_dir_list = list_all_dir_name(dir_name_one) 

for i in comparing_dir_list:
    if "BasicQlearning" in i:
        file_name20 = i
        method_name20 = "Multi-IQL"
    if "AdhocTD" in i and "AdhocTDActionReuseDecay" not in i and "AdhocTDActionReuseQChange" not in i and "AdhocTDQSharing" not in i:
        file_name21 = i
        method_name21 = "AdhocTD"
    if "AdhocTDQSharing" in i  and str(budget) in i:
        file_name22= i
        method_name22 = "AdhocTD-Q"
    if "PartakerSharerQSharing" in i and str(budget) in i:
        file_name23 = i
        method_name23 = "PSAF" 


file_name_list = [eval("file_name"+str(i)) for i in range(var_length) if eval("file_name"+str(i))!=None]
method_name_list = [eval("method_name"+str(i)) for i in range(var_length) if eval("method_name"+str(i))!=None]


evaluation_datas, evaluation_budgets = read_data(file_name_list, method_name_list)                 
                    
                    
# image dir
# save_fig_dir_name = "/home/cike/桌面/ActionReuse/PP domain/"

save_fig_dir_name = dir_name_one
if not os.path.exists(save_fig_dir_name):
    os.mkdir(save_fig_dir_name)
                 

         
figsize = 6, 5
labelsize = 18

plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300 

parameters = {
    'title': "Four predators Catch One Prey",
    'save_name': 'all-best-compare-',
    'legend_num': [1.02,0,3,0],
    "linestyle": ['-', ":", "-.", "--", '-', ":", "-.", "--", '-', ":", "-.", "--", '-', ":", "-.", "--"],
    "linewidth": 2,
    'colors': ['Grey', 'DeepSkyBlue', 'LimeGreen', 'OrangeRed', 'MediumPurple'][::-1],  # ['#7570b3', '#e7298a', '#66a61e', '#e6ab02', 'magenta', 'teal', '#00FFFF', 'red'],
    'partPic': False,
    'yMinMax':[200, 700],
    'label_font': {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 18,
         },
    'title_font': {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 20,
         },
     'legend_font': 14
}


episode_num = 200


# align data
evaluation_datas_new = align_data(evaluation_datas, episode_num)
evaluation_budgets_new = align_data(evaluation_budgets, episode_num)


#===========================================================================
#================================= desire data =============================
#===========================================================================

episode_num = 100
#================================== Q change ===============================
key_list = ['QChange-0', 'QChange-0.01', 'QChange-0.02', 'QChange-0.03', 'QChange-0.05', 'AdhocTD', 'Multi-IQL']
budget_list = ['QChange-0', 'QChange-0.01', 'QChange-0.02', 'QChange-0.03', 'QChange-0.05', 'AdhocTD']
parameters['save_name'] = 'q-change-'

evaluation_datas_list = [evaluation_datas_new[i] for i in key_list]
evaluation_budgets_list = [evaluation_budgets_new[i] for i in budget_list]

# plot_multi_TG(evaluation_datas_list, episode_num, key_list, parameters, True)
# plot_multi_Budget(evaluation_budgets_list, episode_num, budget_list, parameters, True)


# Initial, Last, Average
for key in key_list:
    print(key+"-Initial:"+str(evaluation_datas[key][0])+"-Last:"+str(evaluation_datas[key][-1])+"-Average:"+str(np.mean(evaluation_datas[key])))

for key in key_list:
    print(key+"-Initial-Last-Average:"+str(round(evaluation_datas[key][0], 3))+"&"+str(round(evaluation_datas[key][-1], 3))+"&"+str(round(np.mean(evaluation_datas[key]), 3)))

#================================== Q change ===============================




#================================== Decay rate ===============================
key_list = ['Decay-0.999', 'Decay-0.99', 'Decay-0.95', 'Decay-0.9', 'Decay-0.8', 'AdhocTD', 'Multi-IQL']
budget_list = ['Decay-0.999', 'Decay-0.99', 'Decay-0.95', 'Decay-0.9', 'Decay-0.8', 'AdhocTD']
parameters['save_name'] = 'decay-rate-'

evaluation_datas_list = [evaluation_datas_new[i] for i in key_list]
evaluation_budgets_list = [evaluation_budgets_new[i] for i in budget_list]

# plot_multi_TG(evaluation_datas_list, episode_num, key_list, parameters, True)
# plot_multi_Budget(evaluation_budgets_list, episode_num, budget_list, parameters, True)

# Initial, Last, Average
for key in key_list:
    print(key+"-Initial:"+str(evaluation_datas[key][0])+"-Last:"+str(evaluation_datas[key][-1])+"-Average:"+str(np.mean(evaluation_datas[key])))

for key in key_list:
    print(key+"-Initial-Last-Average:"+str(round(evaluation_datas[key][0], 3))+"&"+str(round(evaluation_datas[key][-1], 3))+"&"+str(round(np.mean(evaluation_datas[key]), 3)))

#================================== Decay rate ===============================



#================================== Fixed length ===============================
key_list = ['FixedLength-5', 'FixedLength-20', 'FixedLength-50', "FixedLength-100", 'FixedLength-150', 'AdhocTD', 'Multi-IQL']
budget_list = ['FixedLength-5', 'FixedLength-20', 'FixedLength-50', "FixedLength-100", 'FixedLength-150', 'AdhocTD']
parameters['save_name'] = 'fix-len-'

evaluation_datas_list = [evaluation_datas_new[i] for i in key_list]
evaluation_budgets_list = [evaluation_budgets_new[i] for i in budget_list]

# plot_multi_TG(evaluation_datas_list, episode_num, key_list, parameters, True)
# plot_multi_Budget(evaluation_budgets_list, episode_num, budget_list, parameters, True)


# Initial, Last, Average
for key in key_list:
    print(key+"-Initial:"+str(evaluation_datas[key][0])+"-Last:"+str(evaluation_datas[key][-1])+"-Average:"+str(np.mean(evaluation_datas[key])))


for key in key_list:
    print(key+"-Initial-Last-Average:"+str(round(evaluation_datas[key][0], 3))+"&"+str(round(evaluation_datas[key][-1], 3))+"&"+str(round(np.mean(evaluation_datas[key]), 3)))

#================================== Fixed length ===============================



#================================== ALL BEST COMPARE===============================
key_list = ['Multi-IQL', 'AdhocTD', 'QChange-0.01', 'FixedLength-100', 'Decay-0.99']
budget_list = ['AdhocTD', 'QChange-0.01', 'FixedLength-100', 'Decay-0.99']
parameters['save_name'] = 'all-best-compare-'

evaluation_datas_list = [evaluation_datas_new[i] for i in key_list]
evaluation_budgets_list = [evaluation_budgets_new[i] for i in budget_list]

new_key_list = ['Multi-IL-Q(λ)', 'AdhocTD'] + ["AdhocTD-"+i for i in key_list if i not in ['AdhocTD', 'Multi-IQL']]
new_key_list[-2] = 'AdhocTD-ReBudget-100'
new_budget_list = ['AdhocTD'] + ["AdhocTD-"+i for i in budget_list if i not in ['AdhocTD', 'Multi-IQL']]
new_budget_list[-2] = 'AdhocTD-ReBudget-100'

parameters['colors'] = ['Grey', 'Gold', 'LimeGreen', 'OrangeRed', 'MediumPurple']
parameters['linestyle'] = ['-', "-.", ":", "--", '-']
plot_multi_TG(evaluation_datas_list, episode_num, new_key_list, parameters, True)

parameters['colors'] = ['Gold', 'LimeGreen', 'OrangeRed', 'MediumPurple']
parameters['linestyle'] = ["-.", ":", "--", '-']
plot_multi_Budget(evaluation_budgets_list, episode_num, new_budget_list, parameters, True)




# Initial, Last, Average
for key in key_list:
    print(key+"-Initial:"+str(evaluation_datas[key][0])+"-Last:"+str(evaluation_datas[key][-1])+"-Average:"+str(np.mean(evaluation_datas[key])))

#================================== ALL BEST COMPARE===============================

