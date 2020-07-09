# coding=utf8
"""
evaluation the results of pursuit game
"""
import matplotlib.pyplot as plt
import os
import numpy as np


colors = ['r', 'blue', 'green', 'y', 'magenta', 'black']

N = 15
if N == 10:
    dir_name_one = "/home/cike/chauncy/game results/pursuit game/2018年9月19日/10-one goal-2 predators-average 100-ask param 0.7-give param 1.5-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
    dir_name_two = "/home/cike/chauncy/game results/pursuit game/2018年10月14日/10-one goal-2 predators-average 100-ask param 0.7-give param 1.5-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
elif N == 15:
    dir_name_one = "/home/cike/chauncy/game results/pursuit game/2018年9月19日/15-one goal-2 predators-average 100-ask param 0.7-give param 1.5-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
    dir_name_two = "/home/cike/chauncy/game results/pursuit game/2018年10月14日/15-one goal-2 predators-average 100-ask param 0.7-give param 1.5-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"

    

dir_name_new = "/home/cike/chauncy/coding/java/multipursuit/logs/10-one goal-2 predators-average 50-ask param 0.7-give param 1.5-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"


def read_data(dir_name):
    title = dir_name.split("/")[-1]
    dir = os.listdir(dir_name)

    evaluation_data = []
    evaluation_budget = []
    method_name = []

    for i in dir:
        file_name = os.path.join(dir_name, i)
        if os.path.isfile(file_name) and ".py" not in file_name and "readme" not in file_name and "QTable" not in file_name:
            with open(file_name, 'r') as f:
                line_data = []
                line_budget = []
                for line in f.readlines():
                    if ",," in line:
                        list_data = line.strip().split(",,")
                        data = []
                        budget = []
                        # list_data[0] = list_data[0][1:]
                        # list_data[-1] = list_data[-1][:-1]

                        for j in list_data:
                            str_list = eval(j)
                            # print(str_list)
                            data.append(str_list[0])
                            budget.append(np.mean([float(str_list[1]), float(str_list[2])]))

                        # evaluate the result each 100 interval
                        new_data = np.array([data[i:i+100] for i in range(len(data)) if i%100 == 0], dtype=np.float)
                        new_budget = np.array([budget[i:i+100] for i in range(len(budget)) if i%100 == 0], dtype=np.float)
                        line_data.append(new_data.mean(axis=1))
                        line_budget.append(new_budget.mean(axis=1))

            # use line data draw the pic
            evaluation_data.append(np.array(line_data).mean(axis=0))
            evaluation_budget.append(np.array(line_budget).mean(axis=0))

            # print(i.split("_"))
            method_name.append(i.split("_")[1])
        else:
            print("Warning: no files match")

    method_name_new = []
    for i in method_name:
        if "Basic" in i:
            method_name_new.append("IQL")
        if "Action" in i:
            method_name_new.append("PSAF")
        if "TD" in i:
            method_name_new.append("AdhocTD")

    return evaluation_data, evaluation_budget, method_name_new, title


evaluation_data_one, evaluation_budget_one, method_name_new_one, title_one = read_data(dir_name_new)
evaluation_data_two, evaluation_budget_two, method_name_new_two, title_two = read_data(dir_name_new)

if method_name_new_one != method_name_new_two or title_one != title_two:
    raise EnvironmentError("wrong input!")

    
evaluation_data = list(np.mean([evaluation_data_one, evaluation_data_two], axis=0))
evaluation_data_n = [0, 0, 0]
evaluation_data_n[0] = evaluation_data[1]
evaluation_data_n[1] = evaluation_data[2]
evaluation_data_n[2] = evaluation_data[0]
evaluation_data = evaluation_data_n

evaluation_budget = list(np.mean([evaluation_budget_one, evaluation_budget_two], axis=0))
evaluation_budget_n = [0, 0, 0]
evaluation_budget_n[0] = evaluation_budget[1]
evaluation_budget_n[1] = evaluation_budget[2]
evaluation_budget_n[2] = evaluation_budget[0]
evaluation_budget = evaluation_budget_n

method_name_new = method_name_new_one
method_name_new_n = [0, 0, 0]
method_name_new_n[0] = method_name_new[1]
method_name_new_n[1] = method_name_new[2]
method_name_new_n[2] = method_name_new[0]
method_name_new = method_name_new_n


title = title_one


plt.figure()
for i in range(len(evaluation_data)):
    plt.plot(range(len(evaluation_data[i])), evaluation_data[i], label=method_name_new[i], color=colors[i])

plt.ylabel("Time to Goal")
plt.xlabel("x100 Traning Episodes")
plt.title("Predator-Prey domain N="+str(N))
plt.legend()
plt.savefig("/home/cike/chauncy/coding/spyder/multiagent/pursuitData/image/"+title + " episodes.png")
plt.show()

evaluation_data_5000 = list(np.array(evaluation_data)[:, :120])
plt.figure()
for i in range(len(evaluation_data_5000)):
    plt.plot(range(len(evaluation_data_5000[i])), evaluation_data_5000[i], label=method_name_new[i], color=colors[i])

plt.ylabel("Time to Goal")
plt.xlabel("x100 Traning Episodes")
plt.title("Predator-Prey domain N="+str(N))
plt.legend()
plt.savefig("/home/cike/chauncy/coding/spyder/multiagent/pursuitData/image/"+title + " episodes_5000.png")
plt.show()


plt.figure()
for i in range(len(evaluation_budget)):
    plt.plot(range(len(evaluation_budget[i])), evaluation_budget[i], label=method_name_new[i], color=colors[i])

plt.ylabel("Budget")
plt.xlabel("x100 Traning Episodes")
plt.title("Predator-Prey domain N="+str(N))
plt.legend()
plt.savefig("/home/cike/chauncy/coding/spyder/multiagent/pursuitData/image/"+title+ " budgets.png")
plt.show()


evaluation_budget_5000 = list(np.array(evaluation_budget)[:, :120])
plt.figure()
for i in range(len(evaluation_budget_5000)):
    plt.plot(range(len(evaluation_budget_5000[i])), evaluation_budget_5000[i], label=method_name_new[i], color=colors[i])

plt.ylabel("Budget")
plt.xlabel("x100 Traning Episodes")
plt.title("Predator-Prey domain N="+str(N))
plt.legend()
plt.savefig("/home/cike/chauncy/coding/spyder/multiagent/pursuitData/image/"+title+ " budgets_5000.png")
plt.show()















