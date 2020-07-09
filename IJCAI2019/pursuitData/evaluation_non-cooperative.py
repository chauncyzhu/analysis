# coding=utf8
"""
evaluation the results of pursuit game
"""
import matplotlib.pyplot as plt
import os
import numpy as np


colors = ['#7570b3', '#e7298a', '#e6ab02', 'magenta', 'black']
eval_interval = 20
method_rank = ['PSAF', 'AdhocTD', 'Multi-IQL']

budget = 2000
N1 = 200
N2 = 300
N3 = 500

    
# different interval
dir_name_one_N0 = "/home/cike/chauncy/game results/pursuit game/levelLearning_20190221/LevelLearning_agent2 0-agent3 0_15-one goal-3 predators-average 50-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"

# agent 100, agent 200
dir_name_one_N1 = "/home/cike/chauncy/game results/pursuit game/levelLearning_20190221/LevelLearning_agent2 100-agent3 200_15-one goal-3 predators-average 500-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"

# agent 100, agent 300
dir_name_one_N2 = "/home/cike/chauncy/game results/pursuit game/levelLearning_20190221/LevelLearning_agent2 100-agent3 300_15-one goal-3 predators-average 500-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"

# agent 100, agent 500
dir_name_one_N3 = "/home/cike/chauncy/game results/pursuit game/levelLearning_20190221/LevelLearning_agent2 100-agent3 500_15-one goal-3 predators-average 500-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"


    
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


evaluation_data_one_N0, evaluation_budget_one_N0, method_name_new_one_N0, title_one_N0 = read_data(dir_name_one_N0)
evaluation_data_N0, evaluation_budget_N0 = getNewDataBudget([evaluation_data_one_N0], [evaluation_budget_one_N0], method_name_new_one_N0, method_rank)
    
    

# N=10    
evaluation_data_one_N1, evaluation_budget_one_N1, method_name_new_one_N1, title_one_N1 = read_data(dir_name_one_N1)
evaluation_data_N1, evaluation_budget_N1 = getNewDataBudget([evaluation_data_one_N1], [evaluation_budget_one_N1], method_name_new_one_N1, method_rank)


# N=10
evaluation_data_one_N2, evaluation_budget_one_N2, method_name_new_one_N2, title_one_N2 = read_data(dir_name_one_N2)
evaluation_data_N2, evaluation_budget_N2 = getNewDataBudget([evaluation_data_one_N2], [evaluation_budget_one_N2], method_name_new_one_N2, method_rank)


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

        
method_name_new_N0, method_name_new_N1, method_name_new_N2, method_name_new_N3 = method_rank.copy(), method_rank.copy(), method_rank.copy(), method_rank.copy()    
method_name_N0 = rename(method_name_new_N0)
method_name_N1 = rename(method_name_new_N1)
method_name_N2 = rename(method_name_new_N2)
method_name_N3 = rename(method_name_new_N3)

                    
                    
                    

                    
# image dir
total_dir_name = "/home/cike/chauncy/game results/pursuit game/different budgets/"
detail_episodes = 100                    


save_fig_dir_name = "/home/cike/桌面/image_total/"
if not os.path.exists(save_fig_dir_name):
    os.mkdir(save_fig_dir_name)
                 

                    
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
        plt.savefig(save_fig_dir_name + "Level_TG_" + str(episodes)+".png", bbox_inches = 'tight')
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
        plt.savefig(save_fig_dir_name + "Level_Budget_" + str(episodes) + ".png", bbox_inches = 'tight')
    plt.show()

# plot_one_TG(evaluation_data_N1, 500, method_name_new_N1)
# plot_one_Budget(evaluation_budget_N1, 500, method_name_new_N1)



    
def plot_multi_TG(data_list, episodes, method_name_list, legend_num, label_text, label_point, label_point_final, save=False):
    data_list = list(np.array(data_list)[:, :, :episodes])
    figure, ax = plt.subplots(figsize = figsize)
    for i, data in enumerate(data_list):
        for j, line in enumerate(data):
            line = list(np.array(line))
            if i == 2:
                plt.plot(range(len(line)), line, linewidth=3, label=method_name_list[i][j], color=colors[j])
            elif i == 0:
                plt.plot(range(len(line)), line, linewidth=3, label=method_name_list[i][j], color=colors[j], 
                     linestyle=linestyle[i])
            else:
                plt.plot(range(len(line)), line, linewidth=3, label=method_name_list[i][j], color=colors[j], 
                     marker=marker[i], markerfacecolor='w', 
                      markersize=3.5, markeredgecolor=colors[j])
        # budget_dot
        plt.annotate(label_text[i],xy=(label_point[i][0], label_point[i][1]),xytext=(label_point_final[i][0], label_point_final[i][1]),arrowprops=dict(arrowstyle="<-",connectionstyle="arc"), size=annotate_size) 



    plt.ylabel("Time to Goal", font2)
    plt.xlabel("x100 Traning Episodes", font2)
    plt.title("Predator-Prey domain", font1)
    
    
    
    plt.legend(fontsize=15, bbox_to_anchor=(legend_num[0], legend_num[1]), loc=legend_num[2], borderaxespad=legend_num[3])
    plt.tick_params(labelsize=labelsize)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    
    if save:
        plt.savefig(save_fig_dir_name + "Level-TG-" + str(episodes)+"-"+str(N1)+"-"+str(N2)+"-"+str(N3)+".png", bbox_inches = 'tight')
    plt.show()



def plot_multi_Budget(data_list, episodes, method_name_list, legend_num, label_text, label_point, label_point_final, save=False):
    data_list = list(np.array(data_list)[:, :, :episodes])
    figure, ax = plt.subplots(figsize = figsize)
    for i, data in enumerate(data_list):
        for j, line in enumerate(data):
            line = list(np.array(line)/divid_budget)
            if j == len(data)-1:
                if i == 2:
                    plt.plot(range(2), [0]*2, linewidth=1.5, label=method_name_list[i][j], color=colors[j])
                elif i==1:
                    plt.plot(range(2), [0]*2, label=method_name_list[i][j], color=colors[j], 
                         linewidth=2, linestyle=linestyle[i])
                else:
                    plt.plot(range(2), [0]*2, linewidth=1.5, label=method_name_list[i][j], color=colors[j], 
                         marker=marker[i], markerfacecolor='w', 
                          markersize=3.5, markeredgecolor=colors[j])
            else: 
                if i == 2:
                    plt.plot(range(len(line)), line, linewidth=1.5, label=method_name_list[i][j], color=colors[j])
                elif i==1:
                    plt.plot(range(len(line)), line, label=method_name_list[i][j], color=colors[j], 
                         linewidth=2, linestyle=linestyle[i])
                else:
                    plt.plot(range(len(line)), line, linewidth=1.5, label=method_name_list[i][j], color=colors[j], 
                         marker=marker[i], markerfacecolor='w', 
                          markersize=3.5, markeredgecolor=colors[j])
        # budget_dot
        plt.annotate(label_text[i],xy=(label_point[i][0], label_point[i][1]),xytext=(label_point_final[i][0], label_point_final[i][1]),arrowprops=dict(arrowstyle="<-",connectionstyle="arc"), size=annotate_size) 



    plt.ylabel("Budget", font2)
    plt.xlabel("x100 Traning Episodes", font2)
    plt.title("Predator-Prey domain", font1)
    
    
    
    plt.legend(bbox_to_anchor=(legend_num[0], legend_num[1]), loc=legend_num[2], borderaxespad=legend_num[3])
    plt.tick_params(labelsize=labelsize)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    
    if save:
        plt.savefig(save_fig_dir_name + "Level-Budget-" + str(episodes)+"-"+str(N1)+"-"+str(N2)+"-"+str(N3)+".png", bbox_inches = 'tight')
    plt.show()


marker = ["o", "o", "*"]
linestyle = ["--", "--", "-."]

legend_num = [1.02,0,3,0]
annotate_size = 18


divid_budget = 1
label_point = [[10, 750], [16, 610], [26, 500]]
label_point_final = [[30, 745], [36, 605], [46, 495]]
label_text = ["dash:200 episodes", "hollow:300 episodes", "solid:500 episodes"]


plot_multi_TG([evaluation_data_N0, evaluation_data_N1, evaluation_data_N2, evaluation_data_N3], 500, 
              [method_name_new_N1,method_name_new_N2, method_name_new_N3], 
              legend_num, label_text, label_point, label_point_final, True)




# budget = inf
divid_budget = 1
bud_label_point = [[395, 160], [100, 220], [135, 40]]
bud_label_point_final = [[300, 100], [8, 270], [200, 40]]
bud_label_text = ["agent 3-200", "agent 3-300", "agent 3-500"]


plot_multi_Budget([evaluation_budget_N1, evaluation_budget_N2, evaluation_budget_N3], 500, 
              [method_name_new_N1,method_name_new_N2, method_name_new_N3], 
              legend_num, bud_label_text, bud_label_point, bud_label_point_final, True)





