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
dir_name = "/home/cike/chauncy/coding/java/multipursuit/logs/10-one goal-2 predators-average 1-ask param 0.7-give param 1.5-reward 0 1-askConfType B-giveConfType A-1-giveConfConstant 2_20180508"
dir_files = os.listdir(dir_name)
dir_files = sorted(dir_files, key=lambda x:int(x.split("_")[-1]))
######merge data######
QData_agent1_list = []
QData_agent2_list = []

# AdhocTD_allQChanges
# AdhocAbsorbReplaceActionConf_allQChanges
data_name = "AdhocTD_allQChanges"

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
        QData_agent1 = QData[:QData.index("agent")]
        QData_agent2 = QData[QData.index("agent")+1:]
        QData_agent1_list.append(QData_agent1)
        QData_agent2_list.append(QData_agent2)
        
        QData = None
        QData_agent1 = None
        QData_agent2 = None


def merge_and_split(QData_list):
    QData_map = {}
    QData_index_map = {}
    for index, QD in enumerate(QData_list):
        print("index:", index)
        for line in QD:
            key = line.split(":")[0]
            try:
                value = line.split(":")[1]
                value = value.split("|")
            except:
                print("wrong:",line)
                raise(Exception("wrong"))                
            
            # store the index of episode and step
            #value_zero = value[0].split(",,")[-1].split(",")
            #value[0] = ",,".join(value[0].split(",,")[:-1]) + ",,-1"
            
            value = list(map(lambda x:x.split(",,"), value))
            if key in QData_map:
                QData_map[key] = QData_map[key] + value                
            else:
                QData_map[key] = value
    return QData_map, QData_index_map

QData_agent1_map = merge_and_split(QData_agent1_list)
QData_agent1_list = None
del QData_agent1_list
# store Q values
store_file = open("/home/cike/chauncy/coding/spyder/multiagent/pursuitData/data/"+data_name+"_agent1", "wb")
pkl.dump(QData_agent1_map, store_file)
QData_agent1_map = None
del QData_agent1_map

QData_agent2_map = merge_and_split(QData_agent2_list)
QData_agent2_list = None
del QData_agent2_list
# store Q values
store_file = open("/home/cike/chauncy/coding/spyder/multiagent/pursuitData/data/"+data_name+"_agent2", "wb")
pkl.dump(QData_agent2_map, store_file)
QData_agent2_map = None
del QData_agent2_map

















