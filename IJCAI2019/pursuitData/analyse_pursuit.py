# -*- coding: utf-8 -*-
import numpy as np
import os
import matplotlib.pyplot as plt
import pickle as pkl
"""
BasicQLearningAdhocAbsorbReplaceActionVisit
BasicQLearningwithAdhocTD
BasicQLearningwithAdhocAbsorbReplace
BasicQLearningAdhocAbsorbMaxReplace
BasicQLearningAdhocAbsorbStateActionVReplace
BasicQLearning 
"""
usableActions = ["UP", "DOWN", "LEFT", "RIGHT", "STAY"]

# reward 5 0
# dir_name = "/home/cike/chauncy/coding/java/multipursuit/logs/10-one goal-2 predators-average 1-ask param 1.0-give param 1.0-reward 5 5-askConfType B-giveConfType A_20180508/"

# reward 1 -1
dir_name = "/home/cike/chauncy/coding/spyder/IJCAI2019/pursuitData/data/old_goal_1114/"
img_name = "/home/cike/chauncy/coding/spyder/IJCAI2019/pursuitData/image/"


# AdhocAbsorbReplaceActionConf_allQChanges_agent1
# AdhocTD_allQChanges_agent1
# AdhocAbsorbReplaceStateConf_allQChanges_agent1
data_1 = "AdhocTD_allQChanges_agent1"
data_2 = "AdhocTD_allQChanges_agent2"

QData_agent1_map = None
QData_agent1_index_map = None
QData_agent2_map = None
QData_agent2_index_map = None

dir_files = os.listdir(dir_name)

for i in dir_files:
    if data_1 in i:   # _AdhocAbsorbReplaceStateConf_allQChanges_    _BasicQLearning_
        file_path = os.path.join(dir_name, i)
        print(file_path)
        QData = pkl.load(open(file_path, "rb"), encoding="utf8")
        QData_agent1_map, QData_agent1_index_map = QData[0], QData[1]
    if data_2 in i:   # _AdhocAbsorbReplaceStateConf_allQChanges_    _BasicQLearning_
        file_path = os.path.join(dir_name, i)
        QData = pkl.load(open(file_path, "rb"), encoding="utf8")
        QData_agent2_map, QData_agent2_index_map = QData[0], QData[1]

"""
temp = QData_agent2_map
QData_agent2_map = QData_agent1_map
QData_agent1_map = temp

temp = QData_agent2_index_map
QData_agent2_index_map = QData_agent1_index_map
QData_agent1_index_map = temp
"""
############################ agent1's state values ############################   
"""
agent1_len_map = {}
for key, value in QData_agent1_map.items():
    agent1_len_map[key] = len(value)
# sort the values
agent1_len_list = sorted(agent1_len_map.items(), key=lambda x:x[1])[::-1]
agent1_max = agent1_len_list[3]
agent1_values = np.array(QData_agent1_map[agent1_max[0]], dtype=np.float32).T[:-1]
agent1_advised = np.array(QData_agent1_map[agent1_max[0]], dtype=np.int32).T[-1]
"""

# find the state which has the most advised value
agent1_advised_list = []
for key, value in QData_agent1_index_map.items():
    advised = np.array(value, dtype=np.float32).T[0]
    count_non_negtive = 0
    for i in advised:
        if i != -1:
            count_non_negtive += 1
    agent1_advised_list.append((key, count_non_negtive))
agent1_advised_list = sorted(agent1_advised_list, key=lambda x:x[1])[::-1]

                             
agent1_episode_list = []
for key, value in QData_agent1_index_map.items():
    episode = np.array(value, dtype=np.float32).T[1]
    agent1_episode_list.append((key, episode[0]))
agent1_episode_list = sorted(agent1_episode_list, key=lambda x:x[1])

                              
# now_key = agent1_episode_list[21][0]   # 11-1216118   1-1031995
# now_key = "1036481"  # 1036481   1095841   # 14
# for agent1:'-1,-2,0,-2' '1,-1,2,-1'  '1,1,0,1'  '0,-2,1,-2'  '1,1,1,2'# very important


# for agent2: -3,2,-3,1; 2,0,2,1; '-1,0,0,1'    use '2,0,2,1'

# --1,-1,-1,0; 1,1,2,1
# -1,0,-1,1
now_key = '0,2,0,1'   # very important
# now_key = '-1,0,-1,1'   # very important


print(now_key)
############################ agent1's prepare values ############################    
QData_agent1 = np.array(QData_agent1_map[now_key], dtype=np.float32)
QData_agent1.shape
agent1_values = QData_agent1[:, 0, :].T
agent1_peer_values = QData_agent1[:, 1, :].T   # peer's Q values in agent1's state
agent1_peer_state_values = QData_agent1[:, 2, :].T   # peer's Q values in agent1's state
agent1_advised = np.array(QData_agent1_index_map[now_key], dtype=np.int32).T
                          
# prepare the point
agent1_advised_point = []
agent1_advised_action = []
for index, value in enumerate(agent1_advised[0]):
    if value != -1:
        agent1_advised_point.append([index, agent1_values[value][index]])  
        agent1_advised_action.append([index, value])

agent1_peer_point = []
for index, value in enumerate(agent1_advised[0]):
    if value != -1:
        agent1_peer_point.append([index, agent1_peer_values[value][index]])  
############################ agent1's prepare values ############################    


font1 = {'family': 'Times New Roman',
         'weight': 'bold',
         'size': 18,
         }
                    
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 22,
         }
annotate_size = 20
labelsize = 20
linestyle=['-', '--', '-.', ':', '-']


"""
figure, ax = plt.subplots(figsize=[8, 6])

parameters:-1,0,-1,1
AdhocTD
final_left = -50
final_right = 0.4
only_num = 300

PSAF
final_left = -50
final_right = 0.4
only_num = 280

plt.xticks(np.arange(0, 400, 100))
plt.yticks(np.arange(0, 4, 0.5))

****************************************************
figure, ax = plt.subplots(figsize=[9, 6])

parameters:0,2,0,1
AdhocTD
final_left = -5
final_right = 0.15
only_num = 35


plt.xticks(np.arange(0, 50, 10))
plt.yticks(np.arange(0, 1.0, 0.2))


PSAF
final_left = -5
final_right = 0.4
only_num = 40

plt.xticks(np.arange(0, 50, 10))
plt.yticks(np.arange(0, 1.4, 0.2))
"""

transparent = False
final_left = -5
final_right = 0.15
only_num = 35
############################ plot state values ############################    
# changes of all Q values
figure, ax = plt.subplots(figsize=[9, 6])
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300 
scatter_s = 250


for index, i in enumerate(agent1_values):
    part_val = i[:only_num]
    if index==4:
        plt.plot(range(len(part_val)), part_val, linewidth=1.5, 
             label=usableActions[index], linestyle=linestyle[index], zorder=10)
    else:
        plt.plot(range(len(part_val)), part_val, linewidth=5, 
             label=usableActions[index], linestyle=linestyle[index], zorder=10)

        
"""
for 0 2 0 1
plt.scatter(list(np.array(agent1_advised_point).T[0]), 
                 list(np.array(agent1_advised_point).T[1]), 
                 c="darkorange", marker="x", s=120,
                 label='Q-value of LEFT')
"""
if now_key == '0,2,0,1' and "AdhocTD" in data_1:
    plt.scatter(list(np.array(agent1_advised_point).T[0]), 
                 list(np.array(agent1_advised_point).T[1]), 
                 c="darkorange", marker="*", s=scatter_s,
                 label='Action UP', linewidths=0, zorder=30)

if now_key == '0,2,0,1' and "ActionConf" in data_1:
        plt.scatter(list(np.array(agent1_advised_point).T[0]), 
                 list(np.array(agent1_advised_point).T[1]), 
                 c="darkorange", marker="*", s=scatter_s,
                 label='Q-value of  UP', linewidths=0, zorder=30)



if now_key == '-1,0,-1,1' and "AdhocTD" in data_1:
    plt.scatter(list(np.array(agent1_advised_point).T[0])[:-2], 
                 list(np.array(agent1_advised_point).T[1])[:-2], 
                 c="darkorange", marker="1", s=scatter_s,
                 label='Other actions', zorder=30)
    plt.scatter(list(np.array(agent1_advised_point).T[0])[-2:], 
                 list(np.array(agent1_advised_point).T[1])[-2:], 
                 c="darkorange", marker="*", s=scatter_s,
                 label='Action UP', linewidths=0, zorder=30)
if now_key == '-1,0,-1,1' and "ActionConf" in data_1:
    plt.scatter(list(np.array(agent1_advised_point).T[0])[:-1], 
                 list(np.array(agent1_advised_point).T[1])[:-1], 
                 c="darkorange", marker="1", s=scatter_s,
                 label='Other Q-values', zorder=30)
    plt.scatter(list(np.array(agent1_advised_point).T[0])[-1:], 
                 list(np.array(agent1_advised_point).T[1])[-1:], 
                 c="darkorange", marker="*", s=scatter_s,
                 label='Q-value of RIGHT', linewidths=0, zorder=30)
    



plt.xticks(np.arange(0, 50, 10))
plt.yticks(np.arange(0, 1.0, 0.2))

begin_episode = str(QData_agent1_index_map[now_key][0][1])+" episode "+str(QData_agent1_index_map[now_key][0][2])+" step"
                
                                    
# plt.xlabel(str(QData_agent1_index_map[now_key][0][1])+" episode "+str(QData_agent1_index_map[now_key][0][2])+" step", font2)
# plt.title("Q-values of predator 1 in <-1,0,-1,-1>", font2, ha='center')
legend = plt.legend(prop=font1, loc="upper left",ncol=2)
plt.tick_params(labelsize=labelsize)
labels = ax.get_xticklabels() + ax.get_yticklabels()
# print labels
[label.set_fontname('Times New Roman') for label in labels]

advised_dot = np.array(agent1_advised_point).T
if "AdhocTD" in data_1:
    plt.annotate("action",xy=(advised_dot[0][-1], advised_dot[1][-1]),xytext=(advised_dot[0][-1] + final_left, advised_dot[1][-1] + final_right),arrowprops=dict(arrowstyle="->",connectionstyle="arc"), size=annotate_size) 
if "ActionConf" in data_1:
    plt.annotate("Q-value",xy=(advised_dot[0][-1], advised_dot[1][-1]),xytext=(advised_dot[0][-1] + final_left, advised_dot[1][-1] + final_right),arrowprops=dict(arrowstyle="->",connectionstyle="arc"), size=annotate_size) 


if transparent:
    frame = legend.get_frame()
    frame.set_alpha(1)
    frame.set_facecolor('none') # 设置图例legend背景透明

    
if "AdhocTD" in data_1:
    plt.savefig(img_name+now_key+"_"+str(transparent)+"_AdhocTD.png",transparent=transparent)
if "ActionConf" in data_1:
    plt.savefig(img_name+now_key+"_"+str(transparent)+"_PSAF.png",transparent=transparent)

plt.show()


"""
plt.figure()
plt.scatter(list(np.array(agent1_advised_action).T[0]), list(np.array(agent1_advised_action).T[1]), c="r", marker="*")
plt.xlabel(str(QData_agent1_index_map[now_key][0][1])+" episode "+str(QData_agent1_index_map[now_key][0][2])+" step")
plt.title("changes of agent 1's advised point")
plt.legend(loc='best')
plt.show()
"""

figure, ax = plt.subplots(figsize=[7, 6])

for index, i in enumerate(agent1_peer_values):
    part_val = i[:only_num]
    plt.plot(range(len(part_val)), part_val, linewidth=1.5, label=usableActions[index])


plt.scatter(list(np.array(agent1_peer_point).T[0]), list(np.array(agent1_peer_point).T[1]), 
                 c="r", marker="*", alpha=0.5,linewidths=0)
plt.xlabel(str(QData_agent1_index_map[now_key][0][1])+" episode "+str(QData_agent1_index_map[now_key][0][2])+" step", font2)
# plt.title("Q-values of predator 2 in <-1,0,-1,-1>", font2)
legend = plt.legend(prop=font1, loc="best")
plt.tick_params(labelsize=labelsize)
labels = ax.get_xticklabels() + ax.get_yticklabels()
# print labels
[label.set_fontname('Times New Roman') for label in labels]

# advised_dot = np.array(agent1_peer_point).T
# plt.annotate("action",xy=(advised_dot[0][-1], advised_dot[1][-1]+0.05),xytext=(advised_dot[0][-1]-7, advised_dot[1][-1]+0.1),arrowprops=dict(arrowstyle="->",connectionstyle="arc"), size=annotate_size) 
frame = legend.get_frame()
frame.set_alpha(1)
frame.set_facecolor('none') # 设置图例legend背景透明


if "AdhocTD" in data_1:
    plt.savefig(img_name+now_key+"_AdhocTD_peer.png",transparent=True)
if "ActionConf" in data_1:
    plt.savefig(img_name+now_key+"_PSAF_peer.png",transparent=True)

plt.show()


"""
plt.figure(figsize=[12, 8])
for index, i in enumerate(agent1_peer_state_values):
    plt.plot(range(len(i)), i, label=usableActions[index])
# plt.scatter(list(np.array(agent1_peer_point).T[0]), list(np.array(agent1_peer_point).T[1]), c="r", marker="*")
plt.xlabel(str(QData_agent1_index_map[now_key][0][1])+" episode "+str(QData_agent1_index_map[now_key][0][2])+" step")
plt.title("changes of agent 1 peer current state's Q values")
plt.legend(loc='best')
plt.show()



plt.figure(figsize=[12, 8])
max_action = list(np.argmax(agent1_peer_state_values, axis=0))
plt.plot(range(len(max_action)), max_action)
# plt.scatter(list(np.array(agent1_peer_point).T[0]), list(np.array(agent1_peer_point).T[1]), c="r", marker="*")
plt.xlabel(str(QData_agent1_index_map[now_key][0][1])+" episode "+str(QData_agent1_index_map[now_key][0][2])+" step")
plt.title("changes of agent 1 peer current action")
plt.legend(loc='best')
plt.show()
"""
############################ agent1's state values ############################    



############################ agent2's prepare values ############################  
QData_agent2 = np.array(QData_agent2_map[now_key], dtype=np.float32)
QData_agent2.shape
agent2_values = QData_agent2[:, 0, :].T
agent2_peer_values = QData_agent2[:, 1, :].T
agent2_advised = np.array(QData_agent2_index_map[now_key], dtype=np.int32).T

# prepare the point
agent2_advised_point = []
agent2_advised_action = []
for index, value in enumerate(agent2_advised[0]):
    if value != -1:
        agent2_advised_point.append([index, agent2_values[value][index]])
        agent2_advised_action.append([index, value])
############################ agent2's prepare values ############################  
                          

                          
############################ agent2's state values ############################  
"""
plt.figure()
for index, i in enumerate(agent2_values):
    plt.plot(range(len(i)), i, label=usableActions[index])

plt.scatter(list(np.array(agent2_advised_point).T[0]), list(np.array(agent2_advised_point).T[1]), c="r", marker="*")
plt.xlabel(str(QData_agent2_index_map[now_key][0][1])+" episode "+str(QData_agent2_index_map[now_key][0][2])+" step")
plt.title("changes of agent 2's Q values")
plt.legend(loc='best')
plt.show()

plt.figure()
plt.scatter(list(np.array(agent2_advised_action).T[0]), list(np.array(agent2_advised_action).T[1]), c="r", marker="*")
plt.xlabel(str(QData_agent2_index_map[now_key][0][1])+" episode "+str(QData_agent2_index_map[now_key][0][2])+" step")
plt.title("changes of agent 2's advised point")
plt.legend(loc='best')
plt.show()
"""
############################ agent2's state values ############################    



# the state of the key
"""
for i in range(-9,9):
    for j in range(-9, 9):
        for k in range(-9, 9):
            for r in range(-9, 9):
                if (i + 19) * 1 + (j + 19) * 39 + (k + 19) * 1521 + (r + 19) * 59319 == int(now_key):
                    print(i, j, k, r)
"""


"""
############################ agent1's different kind of state values ############################    
# changes of maximum Q value and minimum Q value
diffQ = []
maxQ = []
for index, i in enumerate(agent1_values.T):
    diffQ.append(abs(max(i) - min(i)))
    maxQ.append(max(i))
plt.figure()
plt.plot(range(len(diffQ)), diffQ, label="diffQ")
plt.title("changes of agent 1's diffQ values")
plt.legend(loc='best')
plt.show()

# changes of maximum Q value
plt.figure()
plt.plot(range(len(maxQ)), maxQ, label="maxQ")
plt.title("changes of agent 1's maximum values")
plt.legend(loc='best')
plt.show()

# changes of our formular
diffQ = np.array(diffQ)
maxQ = np.array(maxQ)
plt.figure() 
plt.plot(range(len(diffQ)), diffQ/(diffQ + 2), label="diffQ/ (diffQ + 2 )")
plt.title("changes of agent 1's in our formular")
plt.legend(loc='best')
plt.show()
############################ agent1's different kind of state values ############################    



############################ agent2's different kind of state values ############################    
# changes of maximum Q value and minimum Q value
diffQ = []
maxQ = []
for index, i in enumerate(agent2_values.T):
    diffQ.append(abs(max(i) - min(i)))
    maxQ.append(max(i))

plt.figure()
plt.plot(range(len(diffQ)), diffQ, label="diffQ")
plt.title("changes of agent 2's diffQ values")
plt.legend(loc='best')
plt.show()

# changes of maximum Q value
plt.figure()
plt.plot(range(len(maxQ)), maxQ, label="maxQ")
plt.title("changes of agent 2's maximum values")
plt.legend(loc='best')
plt.show()


# changes of our formular
diffQ = np.array(diffQ)
maxQ = np.array(maxQ)
plt.figure() 
plt.plot(range(len(diffQ)), diffQ/(diffQ + 2), label="diffQ/ (diffQ + 2 )")
plt.title("changes of agent 2's in our formular")
plt.legend(loc='best')
plt.show()
############################ agent2's different kind of state values ############################    
"""



