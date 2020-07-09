# coding=utf8
"""
evaluation the results of pursuit game
"""
import matplotlib.pyplot as plt
import os
import numpy as np


colors = ['#7570b3', '#e7298a', '#66a61e', '#e6ab02', 'magenta', 'black']
eval_interval = 100
method_rank = ['PSAF', 'AdhocTD', 'AdhocTD-Q', 'Multi-IQL']

"""
budget_N1 = 1800
budget_N2 = 2200
budget_N3 = 2600
"""

budget_N1 = "inf"
budget_N2 = "inf"
budget_N3 = "inf"

N1=10
N2=12
N3=15

"""
if N == 10:
    dir_name_one = "/home/cike/chauncy/game results/pursuit game/2018年9月19日/10-one goal-2 predators-average 100-ask param 0.7-give param 1.5-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
    dir_name_two = "/home/cike/chauncy/game results/pursuit game/2018年10月14日/10-one goal-2 predators-average 100-ask param 0.7-give param 1.5-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
elif N == 15:
    dir_name_one = "/home/cike/chauncy/game results/pursuit game/2018年9月19日/15-one goal-2 predators-average 100-ask param 0.7-give param 1.5-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
    dir_name_two = "/home/cike/chauncy/game results/pursuit game/2018年10月14日/15-one goal-2 predators-average 100-ask param 0.7-give param 1.5-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
"""


if N1 == 10:
    # dir_name_new = "/home/cike/chauncy/coding/java/multipursuit/logs/10-one goal-2 predators-average 200-ask param 1.0-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
    # dir_name_new = "/home/cike/chauncy/game results/pursuit game/2018年10月20日_new goal/10-one goal-2 predators-average 200-ask param 1.0-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
    # dir_name_new = "/home/cike/chauncy/coding/java/multipursuit/logs/10-one goal-2 predators-average 5-ask param 1.0-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
    # dir_name_one = "/home/cike/chauncy/coding/java/multipursuit/logs/10-one goal-2 predators-average 100-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
    # dir_name_one = "/home/cike/chauncy/coding/java/multipursuit/logs/10-one goal-2 predators-average 200-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
    # dir_name_one = "/home/cike/chauncy/coding/java/multipursuit/logs/10-one goal-2 predators-average 10-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
    
    # different budgets
    # budget inf
    if budget_N1 == "inf":
        dir_name_one_N1 = "/home/cike/chauncy/game results/pursuit game/different budgets/10-one goal-2 predators-average 100-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
    
    # budget 300
    if budget_N1==300:
        dir_name_one_N1 = "/home/cike/chauncy/game results/pursuit game/different budgets/10-one goal-2 predators-average 100-budget300-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
    
    # budget 1800
    if budget_N1==1800:
        dir_name_one_N1 = "/home/cike/chauncy/game results/pursuit game/different budgets/10-one goal-2 predators-average 100-budget1800-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
    
    
    
if N2 == 12:
    # dir_name_new = "/home/cike/chauncy/game results/pursuit game/2018年10月20日_new goal/12-one goal-2 predators-average 200-ask param 1.0-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
    # dir_name_one  = "/home/cike/chauncy/coding/java/multipursuit/logs/12-one goal-2 predators-average 100-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
    # dir_name_one = "/home/cike/chauncy/coding/java/multipursuit/logs/12-one goal-2 predators-average 200-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"

    # different budgets
    # budget inf
    if budget_N2 == "inf":
        dir_name_one_N2 = "/home/cike/chauncy/game results/pursuit game/different budgets/12-one goal-2 predators-average 50-budget2147483647-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
        dir_name_two_N2 = "/home/cike/chauncy/game results/pursuit game/different budgets/12-one goal-2 predators-average 50-budget2147483647-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20190221"
    
    # budget 2200
    if budget_N2 == 2200:
        dir_name_one_N2 = "/home/cike/chauncy/game results/pursuit game/different budgets/12-one goal-2 predators-average 50-budget2200-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
        dir_name_two_N2 = "/home/cike/chauncy/game results/pursuit game/different budgets/12-one goal-2 predators-average 50-budget2200-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20190221"
    
    # budget 800
    if budget_N2 == 800:
        dir_name_one_N2 = "/home/cike/chauncy/game results/pursuit game/different budgets/12-one goal-2 predators-average 50-budget800-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
        dir_name_two_N2 = "/home/cike/chauncy/game results/pursuit game/different budgets/12-one goal-2 predators-average 50-budget800-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20190221"

if N3 == 15:
    # budget inf
    if budget_N3 == "inf":
        dir_name_one_N3 = "/home/cike/chauncy/game results/pursuit game/different budgets/15-one goal-2 predators-average 50-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
    
    
    # budget 2600
    if budget_N3 == 2600:
        dir_name_one_N3 = "/home/cike/chauncy/game results/pursuit game/different budgets/15-one goal-2 predators-average 50-budget2600-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"
    
    # budget 1000
    if budget_N3 == 1000:
        dir_name_one_N3 = "/home/cike/chauncy/game results/pursuit game/different budgets/15-one goal-2 predators-average 50-budget1000-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"

    
def read_data(dir_name):
    title = dir_name.split("/")[-1]
    dir = os.listdir(dir_name)

    evaluation_data = []
    evaluation_budget = []
    method_name = []

    for i in dir:
        file_name = os.path.join(dir_name, i)
        if os.path.isfile(file_name) and ".py" not in file_name and "readme" not in file_name and "QTable" not in file_name:
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
            evaluation_data.append(one_file_data.mean(axis=0))
            evaluation_budget.append(one_file_budget.mean(axis=0))

            method_name.append(i.split("_")[1])
        else:
            print("Warning: no files match")

            
    method_name_new = []
    for i in method_name:
        if "Basic" in i:
            method_name_new.append("Multi-IQL")
        if "Action" in i:
            method_name_new.append("PSAF")
        if "State" in i:
            method_name_new.append("AdhocTD-Q")
        if "TD" in i:
            method_name_new.append("AdhocTD")
        if "Qvalues" in i:
            method_name_new.append("Early-Q values")

    return evaluation_data, evaluation_budget, method_name_new, title

    
def sort_by_name(data, data_name, name_list):
    new_data = [0]*len(data_name)
    if len(data_name)!=len(name_list):
        return new_data
    for ind,i in enumerate(name_list):
        if i in data_name:
            new_data[ind] = data[data_name.index(i)]
    return new_data


def getNewDataBudget(datalist, budgetlist, method_name, method_rank):
    if len(datalist) == 1:
        datalist = datalist[0]
    else:
        datalist = list(np.mean(datalist, axis=0))    
    datalist = sort_by_name(datalist, method_name, method_rank)
    
    if len(budgetlist) == 1:
        budgetlist = budgetlist[0]
    else:
        budgetlist = list(np.mean(budgetlist, axis=0))
    budgetlist = sort_by_name(budgetlist, method_name, method_rank)

    return datalist, budgetlist


    
    

# N=10    
evaluation_data_one_N1, evaluation_budget_one_N1, method_name_new_one_N1, title_one_N1 = read_data(dir_name_one_N1)
evaluation_data_N1, evaluation_budget_N1 = getNewDataBudget([evaluation_data_one_N1], [evaluation_budget_one_N1], method_name_new_one_N1, method_rank)


# N=10
evaluation_data_one_N2, evaluation_budget_one_N2, method_name_new_one_N2, title_one_N2 = read_data(dir_name_one_N2)
evaluation_data_two_N2, evaluation_budget_two_N2, method_name_new_two_N2, title_two_N2 = read_data(dir_name_two_N2)

evaluation_data_N2, evaluation_budget_N2 = getNewDataBudget([evaluation_data_one_N2, evaluation_data_two_N2], [evaluation_budget_one_N2, evaluation_budget_two_N2], method_name_new_one_N2, method_rank)
method_name_new_N2 = method_rank.copy()


# N=15
evaluation_data_one_N3, evaluation_budget_one_N3, method_name_new_one_N3, title_one_N3 = read_data(dir_name_one_N3)
evaluation_data_N3, evaluation_budget_N3 = getNewDataBudget([evaluation_data_one_N3], [evaluation_budget_one_N3], method_name_new_one_N3, method_rank)


# rename the name of all methods with different N
def rename(name, id_num=None):
    if id_num:
        for i, one in enumerate(name):
            if "PSAF" == one:
                name[i] = "PSAF-"+ str(id_num)
            if "AdhocTD" == one:
                name[i] = "AdhocTD-"+ str(id_num)
            if "AdhocTD-Q" == one:
                name[i] = "AdhocTD-Q-"+ str(id_num)
            if "IQL" in one:
                name[i] = "Multi-IQL-"+ str(id_num)
    return name

        
method_name_new_N1, method_name_new_N2, method_name_new_N3 = method_rank.copy(), method_rank.copy(), method_rank.copy()    
method_name_N1 = rename(method_name_new_N1)
method_name_N2 = rename(method_name_new_N2)
method_name_N3 = rename(method_name_new_N3)

                    
                    
                    
def plot_one_TG(data, episodes, method_name, save=False):
    data = list(np.array(data)[:, :episodes])
    figure, ax = plt.subplots(figsize = figsize)
    for i in range(len(data)):
        plt.plot(range(len(data[i])), data[i], linewidth=1.5, label=method_name[i], color=colors[i])
    
    plt.ylabel("Time to Goal", font2)
    plt.xlabel("x100 Traning Episodes", font2)
    plt.title("Predator-Prey domain", font2)
    plt.legend(prop=font1, loc="best")
    plt.tick_params(labelsize=labelsize)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    
    if save:
        plt.savefig(save_fig_dir_name + "PP_TG_" + str(episodes)+".png", bbox_inches = 'tight')
    plt.show()


    
def plot_one_Budget(budget, episodes, method_name, save=False):
    budget = list(np.array(budget)[:, :episodes])
    figure, ax = plt.subplots(figsize = figsize)
    for i in range(len(budget)-1):
        plt.plot(range(len(budget[i])), budget[i], linewidth=1.5, label=method_name[i], color=colors[i])
    
    plt.ylabel("Budget", font2)
    plt.xlabel("x100 Traning Episodes", font2)
    plt.title("Predator-Prey domain", font2)
    plt.legend(prop=font1, loc="best")
    plt.tick_params(labelsize=labelsize)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    
    if save:
        plt.savefig(save_fig_dir_name + "PP_Budget_" + str(episodes) + ".png", bbox_inches = 'tight')
    plt.show()

# plot_one_TG(evaluation_data_N1, 500, method_name_new_N1)
# plot_one_Budget(evaluation_budget_N1, 500, method_name_new_N1)



                    
# image dir
total_dir_name = "/home/cike/chauncy/game results/pursuit game/different budgets/"
detail_episodes = 100                    

save_fig_dir_name = "/home/cike/桌面/image_total/"
if not os.path.exists(save_fig_dir_name):
    os.mkdir(save_fig_dir_name)
                 


    
def plot_multi_TG(data_list, episodes, method_name_list, label_text, label_point, label_point_final, parameters, save=False):
    data_list = list(np.array(data_list)[:, :, :episodes])
    figure, ax = plt.subplots(figsize = figsize)
    for i, data in enumerate(data_list):
        for j, line in enumerate(data):
            line = list(np.array(line)/100)
            if parameters['marker_or_not'][i]:
                plt.plot(range(len(line)), line, linewidth=parameters['linewidth'][i], 
                    label=method_name_list[i][j], color=colors[j], 
                    marker=parameters['marker'][i], markerfacecolor='w', 
                    markersize=parameters['markersize'][i], markeredgecolor=colors[j], linestyle=parameters['linestyle'][i])
            else:
                plt.plot(range(len(line)), line, linewidth=parameters['linewidth'][i], 
                    label=method_name_list[i][j], color=colors[j], linestyle=parameters['linestyle'][j])
  
        # budget_dot
        plt.annotate(label_text[i],xy=(label_point[i][0], label_point[i][1]),xytext=(label_point_final[i][0], label_point_final[i][1]),
                     arrowprops=dict(arrowstyle="<-",connectionstyle="arc"), 
                        size=annotate_size) 

    plt.ylabel("x100 Time to Goal", font2)
    plt.xlabel("x100 Traning Episodes", font2)
    plt.title("Predator-Prey domain", font1)
    
    # plt.legend(bbox_to_anchor=(legend_num[0], legend_num[1]), loc=legend_num[2], borderaxespad=legend_num[3])
    plt.tick_params(labelsize=labelsize)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    if save:
        plt.savefig(save_fig_dir_name + "PP-TG-" + str(episodes)+"-"+str(budget_N1)+"-"+str(budget_N2)+"-"+str(budget_N3)+"_nolegend.png", bbox_inches = 'tight')
    plt.show()
    

def plot_multi_Budget(data_list, episodes, method_name_list, label_text, label_point, label_point_final, parameters, save=False):
    data_list = list(np.array(data_list)[:, :, :episodes])
    figure, ax = plt.subplots(figsize = figsize)
    for i, data in enumerate(data_list):
        for j, line in enumerate(data):
            line = list(np.array(line)/divid_budget)
            if j == len(data)-1:
                if i == 2:
                    plt.plot(range(2), [0]*2, linewidth=parameters['linewidth'][i], label=method_name_list[i][j], color=colors[j])
                elif i==1:
                    plt.plot(range(2), [0]*2, label=method_name_list[i][j], color=colors[j], 
                         linewidth=parameters['linewidth'][i], linestyle=parameters['linestyle'][j])
                else:
                    plt.plot(range(2), [0]*2, linewidth=parameters['linewidth'][i], label=method_name_list[i][j], color=colors[j], 
                         marker=parameters['marker'][i], markerfacecolor='w', 
                          markersize=3.5, markeredgecolor=colors[j])
            else: 
                if i == 2:
                    plt.plot(range(len(line)), line, linewidth=parameters['linewidth'][i], label=method_name_list[i][j], color=colors[j])
                elif i==1:
                    plt.plot(range(len(line)), line, label=method_name_list[i][j], color=colors[j], 
                         linewidth=parameters['linewidth'][i], linestyle=parameters['linestyle'][j])
                else:
                    plt.plot(range(len(line)), line, linewidth=parameters['linewidth'][i], label=method_name_list[i][j], color=colors[j], 
                         marker=parameters['marker'][i], markerfacecolor='w', 
                          markersize=3.5, markeredgecolor=colors[j], linestyle=parameters['linestyle'][j])
        # budget_dot
        plt.annotate(label_text[i],xy=(label_point[i][0], label_point[i][1]),xytext=(label_point_final[i][0], label_point_final[i][1]),arrowprops=dict(arrowstyle="<-",connectionstyle="arc"), size=annotate_size) 



    plt.ylabel("x"+str(divid_budget)+" Budget", font2)
    plt.xlabel("x100 Traning Episodes", font2)
    plt.title("Predator-Prey domain", font1)
    
    
    plt.legend(bbox_to_anchor=(parameters['legend_num'][0], parameters['legend_num'][1]), fontsize=15.5, 
                               loc=parameters['legend_num'][2], borderaxespad=parameters['legend_num'][3])
    plt.tick_params(labelsize=labelsize)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    
    if save:
        plt.savefig(save_fig_dir_name + "PP-Budget-" + str(episodes)+"-"+str(budget_N1)+"-"+str(budget_N2)+"-"+str(budget_N3)+"_short.png", bbox_inches = 'tight')
    plt.show()


font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 14,
         }
                    
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 22,
         }   
                 
figsize = 6, 5
labelsize = 14

plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300 

annotate_size = 18



parameters = {
    'legend_num': [1.02,0,3,0],
    "marker":["*", "+", "."],
    "linestyle": ['-', "--", "-.", ":"],
    "linewidth":[4, 1, 1],
    'markersize': [3, 3, 5],
    'marker_or_not':[False, False, False]
}


"""
label_point = [[14, 25], [30, 37], [50, 49]]
label_point_final = [[19, 20], [40, 32], [100, 47]]
if budget_N1 == budget_N2 == budget_N3 == "inf": 
    label_text = ["N=10,b=+∞", "N=12, b=+∞", "N=15, b=+∞"]
else:
    label_text = ["N=10,b="+str(budget_N1), "N=12, b="+str(budget_N2), "N=15, b="+str(budget_N3)]


if budget_N1 == budget_N2 == budget_N3 == "inf":
    divid_budget = 1000
    bud_label_point = [[100, 40], [400, 115], [200, 95]]
    bud_label_point_final = [[10, 110], [315, 165], [115, 180]]

if budget_N1 == 1800 and budget_N2 == 2200 and budget_N3 == 2600:
    divid_budget = 10
    bud_label_point = [[395, 160], [100, 220], [135, 40]]
    bud_label_point_final = [[300, 100], [8, 270], [200, 40]]

if budget_N1 == 300 and budget_N2 == 800 and budget_N3 == 1000:
    divid_budget = 10
    bud_label_point = [[300, 30], [300, 80], [75, 10]]
    bud_label_point_final = [[208, 45], [215, 65], [140, 10]]

if budget_N1 == budget_N2 == budget_N3 == "inf": 
    bud_label_text = ["hollow:N=10,b=+∞", "solid:N=12, b=+∞", "dash:N=15, b=+∞"]
else:
    bud_label_text = ["hollow:N=10,b="+str(budget_N1), "dash:N=12, b="+str(budget_N2), "solid:N=15, b="+str(budget_N3)]



plot_multi_TG([evaluation_data_N1, evaluation_data_N2, evaluation_data_N3], 500, 
              [method_name_new_N1,method_name_new_N2, method_name_new_N3], 
              label_text, label_point, label_point_final, parameters, True)



plot_multi_Budget([evaluation_budget_N1, evaluation_budget_N2, evaluation_budget_N3], 500, 
              [method_name_new_N1,method_name_new_N2, method_name_new_N3], 
              bud_label_text, bud_label_point, bud_label_point_final, parameters, True)

"""

label_point = [[14, 25], [30, 37], [50, 49]]
label_point_final = [[19, 20], [40, 32], [100, 47]]
if budget_N1 == budget_N2 == budget_N3 == "inf": 
    label_text = ["N=10,b=+∞", "N=12, b=+∞", "N=15, b=+∞"]
else:
    label_text = ["N=10,b="+str(budget_N1), "N=12, b="+str(budget_N2), "N=15, b="+str(budget_N3)]



# budget = inf
if budget_N1 == budget_N2 == budget_N3 == "inf":
    divid_budget = 1000
    bud_label_point = [[100, 40], [400, 115], [200, 95]]
    bud_label_point_final = [[10, 110], [315, 165], [115, 180]]

if budget_N1 == 1800 and budget_N2 == 2200 and budget_N3 == 2600:
    divid_budget = 10
    bud_label_point = [[395, 160], [100, 220], [135, 40]]
    bud_label_point_final = [[300, 100], [8, 270], [200, 40]]

if budget_N1 == 300 and budget_N2 == 800 and budget_N3 == 1000:
    divid_budget = 10
    bud_label_point = [[300, 30], [300, 80], [75, 10]]
    bud_label_point_final = [[208, 45], [215, 65], [140, 10]]

if budget_N1 == budget_N2 == budget_N3 == "inf": 
    bud_label_text = ["hollow:N=10,b=+∞", "solid:N=12, b=+∞", "dash:N=15, b=+∞"]
else:
    bud_label_text = ["hollow:N=10,b="+str(budget_N1), "dash:N=12, b="+str(budget_N2), "solid:N=15, b="+str(budget_N3)]



plot_multi_TG([evaluation_data_N3], 500, 
              [method_name_new_N3], 
              [label_text[-1]], [label_point[-1]], [label_point_final[-1]], parameters, True)


plot_multi_Budget([evaluation_budget_N3], 500, 
              [method_name_new_N3], 
              [bud_label_text[-1]], [bud_label_point[-1]], [bud_label_point_final[-1]], parameters, True)



