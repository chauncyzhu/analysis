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
dir_name = "/home/cike/chauncy/coding/spyder/multiagent/pursuitData/data/"

# AdhocAbsorbReplaceActionConf_allQChanges_agent1
# AdhocTD_allQChanges_agent1
data_1 = "AdhocAbsorbReplaceActionConf_allQChanges_agent1"
data_2 = "AdhocAbsorbReplaceActionConf_allQChanges_agent2"

QData_agent1_map = None
QData_agent2_map = None

dir_files = os.listdir(dir_name)

for i in dir_files:
    if data_1 in i:   # _AdhocAbsorbReplaceStateConf_allQChanges_    _BasicQLearning_
        file_path = os.path.join(dir_name, i)
        QData_agent1_map = pkl.load(open(file_path, "rb"), encoding="utf8")
    if data_2 in i:   # _AdhocAbsorbReplaceStateConf_allQChanges_    _BasicQLearning_
        file_path = os.path.join(dir_name, i)
        QData_agent2_map = pkl.load(open(file_path, "rb"), encoding="utf8")

        
############################ agent1's state values ############################   
agent1_len_map = {}
for key, value in QData_agent1_map.items():
    agent1_len_map[key] = len(value)

# sort the values
agent1_len_list = sorted(agent1_len_map.items(), key=lambda x:x[1])[::-1]
agent1_max = agent1_len_list[3]

agent1_values = np.array(QData_agent1_map[agent1_max[0]], dtype=np.float32).T[:-1]
agent1_advised = np.array(QData_agent1_map[agent1_max[0]], dtype=np.float32).T[-1]


# find the state which has the most advised value
agent1_advised_list = []
for key, value in QData_agent1_map.items():
    advised = np.array(value, dtype=np.float32).T[-1]
    agent1_advised_list.append((key, np.count_nonzero(advised)))

agent1_advised_list = sorted(agent1_advised_list, key=lambda x:x[1])[::-1]


now_key = agent1_advised_list[10][0]
agent1_values = np.array(QData_agent1_map[now_key], dtype=np.float32).T[:-1]
agent1_advised = np.array(QData_agent1_map[now_key], dtype=np.float32).T[-1]

############################ agent1's state values ############################    



############################ plot state values ############################    
# changes of all Q values
plt.figure()
for index, i in enumerate(agent1_values):
    plt.plot(range(len(i)), i, label=usableActions[index])
# plt.plot(range(len(agent1_advised)), agent1_advised, label="advised", marker="+")    
plt.title("changes of agent 1's Q values")
plt.legend(loc='best')
plt.show()

plt.figure()
plt.plot(range(len(agent1_advised)), agent1_advised, label="advised", marker=".")    
plt.title("changes of agent 1's Q values")
plt.legend(loc='best')
plt.show()

############################ agent1's state values ############################    



############################ agent2's state values ############################       
agent2_cer_values = QData_agent2_map[now_key]
agent2_values = np.array(agent2_cer_values, dtype=np.float32).T[:-1]
agent2_advised = np.array(agent2_cer_values, dtype=np.float32).T[-1]


plt.figure()
for index, i in enumerate(agent2_values):
    plt.plot(range(len(i)), i, label=usableActions[index])
#plt.plot(range(len(agent2_advised)), agent2_advised, label="advised", marker="+")    
plt.title("changes of agent 2's Q values")
plt.legend(loc='best')
plt.show()

plt.figure()
plt.plot(range(len(agent2_advised)), agent2_advised, label="advised", marker=".")    
plt.title("changes of agent 2's Q values")
plt.legend(loc='best')
plt.show()
############################ agent2's state values ############################    



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




