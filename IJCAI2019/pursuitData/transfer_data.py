# -*- coding: utf-8 -*-
import os
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
# dir_name = "/home/cike/chauncy/coding/java/multipursuit/logs/10-one goal-2 predators-average 1-ask param 1.0-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
dir_name = "/home/cike/chauncy/coding/java/multipursuit/logs/10-one goal-2 predators-average 1-ask param 0.7-give param 1.0-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 1_20180508"

dir_files = os.listdir(dir_name)
dir_files = sorted(dir_files, key=lambda x:int(x.split("_")[-1]))
######merge data######
QData_agent1_list = []
QData_agent2_list = []

# AdhocTD_allQChanges
# AdhocAbsorbReplaceActionConf_allQChanges
# AdhocAbsorbReplaceStateConf_allQChanges
data_name = "AdhocAbsorbReplaceStateConf_allQChanges"

for i in dir_files:
    if data_name in i:   # _AdhocAbsorbReplaceStateConf_allQChanges_    _BasicQLearning_
        print(i)
        file_path = os.path.join(dir_name, i)
        QData = open(file_path, 'rb')
        QData = QData.readlines()
        QData = list(map(lambda x:x.decode().strip(), QData))
        
        if "agent" in QData:
            print("agent count:",QData.count("agent"))
            print("true, agent index:",QData.index("agent"), "||total length:",len(QData))
        QData_agent1_list = QData[:QData.index("agent")]
        QData_agent2_list = QData[QData.index("agent")+1:]
        
        QData = None


def transfer_data(QData_list):
    QData_map = {}
    QData_index_map = {}
    for line in QData_list:
        key = line.split(":")[0]
        try:
            value = line.split(":")[1]
            value = value.split("|")
        except:
            print("wrong:",line)
            raise(Exception("wrong"))                
        
        # store the index of episode and step 
        state_list = []
        info_list = []
        for va in value:
            state_va = va.split(",,")[:-1]
            info_va = va.split(",,")[-1].split(",")
            info_va = [int(i) for i in info_va]
                        
            state_va_list = []
            for sv in state_va:
                state_va_list.append([float(ss) for ss in sv.split(",")])            
            state_list.append(state_va_list)
            info_list.append(info_va)     
        
        QData_map[key] = state_list
        QData_index_map[key] = info_list

    return QData_map, QData_index_map

    
QData_agent1_map, QData_agent1_index_map = transfer_data(QData_agent1_list)
QData_agent1_list = None
del QData_agent1_list
# store Q values
store_file = open("/home/cike/chauncy/coding/spyder/multiagent/pursuitData/data/"+data_name+"_agent1", "wb")
pkl.dump([QData_agent1_map, QData_agent1_index_map], store_file)
QData_agent1_map = None
del QData_agent1_map
del QData_agent1_index_map

QData_agent2_map, QData_agent2_index_map = transfer_data(QData_agent2_list)
QData_agent2_list = None
del QData_agent2_list
# store Q values
store_file = open("/home/cike/chauncy/coding/spyder/multiagent/pursuitData/data/"+data_name+"_agent2", "wb")
pkl.dump([QData_agent2_map, QData_agent2_index_map], store_file)
QData_agent2_map = None
del QData_agent2_map
del QData_agent2_index_map








