# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl

# four predators catch one prey
# all_data_dir_name = "/home/cike/IdeaProjects/multipursuit/data/actionvisitMap/10-4 predators-1 average-2147483647 budget-0.2 ask-1.0 give-1 giveCons-2 learningFrame-0 actionVisit-0 stateVisit-false weightedQ_20190603/"

key = "hfo"

if key == "hfo":
    all_data_dir_name = "/home/cike/chauncy/game results/analyse visit times/hfo/"


def parse_data(dir_name):
    all_data_dir = os.listdir(dir_name)
    all_data_list = []
    for i in all_data_dir:
        print("dir name:"+i)
        if i != "share_agentData":
            agents_stateActionVisitMap = []
            agent_name_list = os.listdir(os.path.join(dir_name, i))
            agent_name_list.sort()
            for j in agent_name_list:
                print("agent name:"+j)
                stateActionVisitMap_str = pkl.load(open(os.path.join(dir_name, i, j), 'rb'))
                stateActionVisitMap = {}
                for key in stateActionVisitMap_str.keys():
                    
                    value = stateActionVisitMap_str[key].split("|")
                    all_time = []
                    for val in value:
                        id_visits = stateActionVisitMap_str[key].split(",,")
                        each_time = {}
                        
                        first_one_id = id_visits[0][0]
                        first_one_value = id_visits[0][id_visits[0].index("{")+1:id_visits[0].index("}")]
                        
                        first_one_value = map(lambda x:int(float(x)), first_one_value.split(","))
                        each_time[int(first_one_id)] = list(first_one_value)
                        
                        for sec in id_visits[1:]:
                            curr_value = sec[sec.index("{")+1:sec.index("}")]
                            curr_value = map(lambda x:int(float(x)), curr_value.split(","))
                            each_time[int(sec[0])] = [int(sec[2]), list(curr_value)]
                        
                        all_time.append(each_time)
                        
                    stateActionVisitMap[key] = all_time            
                
                agents_stateActionVisitMap.append(stateActionVisitMap)
            all_data_list.append(agents_stateActionVisitMap)   

    return all_data_list
                       

all_data_list = parse_data(all_data_dir_name)

# statistics
agent_id = 0

adhocTD_data = all_data_list[1][agent_id]
psaf_data = all_data_list[0][agent_id]
adhocTDQ_data = all_data_list[2][agent_id]


"""
=====================================================================================
=====================================================================================
============================count the visit times in each interval===================
=====================================================================================
=====================================================================================
"""
# seg data
interval = 10

# count the number of times that agents advise/share
def getStateVisitDistribution(visit_data):
    advisor_state_visit_distribution = []
    advisee_state_visit_distribution = []

    print(str(len(visit_data))+" states are advised/shared")
    for state in visit_data.keys():
        many_times = visit_data[state]
        for one_time in many_times:
            for one_id in one_time.keys():
                if one_id != agent_id:
                    one_sum_visit = sum(one_time[one_id][1])
                    advisor_state_visit_distribution.append(one_sum_visit)
                else:
                    one_sum_visit = sum(one_time[one_id])
                    advisee_state_visit_distribution.append(one_sum_visit)
                    
    return advisee_state_visit_distribution, advisor_state_visit_distribution

def find(arr,min_v,max_v):
	pos_min = arr>min_v
	pos_max =  arr<max_v
	pos_rst = pos_min & pos_max
	return np.where(pos_rst == True)

def getIntervalList(data_list):
    data_list = np.sort(data_list)
    data_list = [find(data_list, i, i+interval)
                for i in range(max(data_list))[::interval]]
    data_list = list(map(lambda x:len(x[0]), data_list))
    return data_list

adhocTD_advisee_state_visit_distribution, adhocTD_advisor_state_visit_distribution = getStateVisitDistribution(adhocTD_data)
adhocTD_advisee_state_visit_distribution_x = getIntervalList(adhocTD_advisee_state_visit_distribution)
adhocTD_advisor_state_visit_distribution_x = getIntervalList(adhocTD_advisor_state_visit_distribution)


psaf_advisee_state_visit_distribution, psaf_advisor_state_visit_distribution = getStateVisitDistribution(psaf_data)
psaf_advisee_state_visit_distribution_x = getIntervalList(psaf_advisee_state_visit_distribution)
psaf_advisor_state_visit_distribution_x = getIntervalList(psaf_advisor_state_visit_distribution)




save_fig_dir_name = "/home/cike/桌面/"


"""
=====================================================================================
=====================================================================================
=============draw the plot of (x, y)=(advisee_state_times, advisor_state_times)======
=====================================================================================
=====================================================================================
"""

# count the number of times that agents advise/share
def getStateVisitPair(visit_data):
    state_visit_pair = []
    print(str(len(visit_data))+" states are advised/shared")
    for state in visit_data.keys():
        many_times = visit_data[state]
        for one_time in many_times:
            for one_id in one_time.keys():
                if one_id != agent_id:
                    advisee_sum_visit = sum(one_time[agent_id])
                    advisor_sum_visit = sum(one_time[one_id][1])
                    state_visit_pair.append([advisee_sum_visit, advisor_sum_visit])
                    
    return state_visit_pair


parameters = {
    "s": [50, 50, 50],
    'colors': ['#7570b3', '#e7298a', '#66a61e', '#e6ab02', 'magenta', 'black']
    
}
        
font1 = {'family': 'Times New Roman',
 'weight': 'normal',
 'size': 16,
 }



figsize = 7, 5

plt.rcParams['savefig.dpi'] = 150
plt.rcParams['figure.dpi'] = 150 

figure, ax = plt.subplots(figsize = figsize)   
adhocTD_advisee_advisor_pair = np.array(getStateVisitPair(adhocTD_data)).T
plt.scatter(list(adhocTD_advisee_advisor_pair[0]), list(adhocTD_advisee_advisor_pair[1]), s=parameters['s'][0], 
            c='', edgecolors=parameters['colors'][1], marker='o', alpha=0.6, label='AdhocTD')
#plt.show()


adhocTDQ_advisee_advisor_pair = np.array(getStateVisitPair(adhocTDQ_data)).T
plt.scatter(list(adhocTDQ_advisee_advisor_pair[0]), list(adhocTDQ_advisee_advisor_pair[1]), s=parameters['s'][1], 
            c='',edgecolors=parameters['colors'][2], marker='^', alpha=0.6, label='AdhocTD-Q')
#plt.show()


psaf_advisee_advisor_pair = np.array(getStateVisitPair(psaf_data)).T
plt.scatter(list(psaf_advisee_advisor_pair[0]), list(psaf_advisee_advisor_pair[1]), s=parameters['s'][2], 
            color='', edgecolors=parameters['colors'][0], marker='*', alpha=0.6, label='PSAF')


plt.xlabel("visit times of states of partaker", font1)
plt.ylabel("visit times of states of sharer", font1)
plt.title("The distribution of sharing for corresponding states", font1)
plt.legend(loc='best', fontsize=14)

plt.savefig(save_fig_dir_name + key + "-state-visit.eps", bbox_inches = 'tight', format="eps")

plt.show()





"""
=====================================================================================
=====================================================================================
===========draw the plot of (x, y)=(advisee_action_times, advisor_action_times)======
=====================================================================================
=====================================================================================
"""
# count the number of times that agents advise/share
def getStateActionVisitPair(visit_data):
    state_visit_pair = []
    print(str(len(visit_data))+" states are advised/shared")
    for state in visit_data.keys():
        many_times = visit_data[state]
        for one_time in many_times:
            for one_id in one_time.keys():
                if one_id != agent_id:
                    # print("many_times:", many_times)
                    advisee_action_visit = one_time[agent_id][one_time[one_id][0]]
                    advisor_action_visit = one_time[one_id][1][one_time[one_id][0]]
                    state_visit_pair.append([advisee_action_visit, advisor_action_visit])
                    
    return state_visit_pair


parameters = {
    "s": [50, 50, 50],
    'colors': ['#7570b3', '#e7298a', '#66a61e', '#e6ab02', 'magenta', 'black']
    
}
   


figsize = 7, 5

plt.rcParams['savefig.dpi'] = 150
plt.rcParams['figure.dpi'] = 150 

figure, ax = plt.subplots(figsize = figsize) 

adhocTD_advisee_advisor_pair = np.array(getStateActionVisitPair(adhocTD_data)).T
plt.scatter(list(adhocTD_advisee_advisor_pair[0]), list(adhocTD_advisee_advisor_pair[1]), s=parameters['s'][0], 
            c='', edgecolors=parameters['colors'][1], marker='o', alpha=0.6, label='AdhocTD')
#plt.show()


adhocTDQ_advisee_advisor_pair = np.array(getStateActionVisitPair(adhocTDQ_data)).T
plt.scatter(list(adhocTDQ_advisee_advisor_pair[0]), list(adhocTDQ_advisee_advisor_pair[1]), s=parameters['s'][1], 
            c='', edgecolors=parameters['colors'][2], marker='^', alpha=0.6, label='AdhocTD-Q')
#plt.show()


psaf_advisee_advisor_pair = np.array(getStateActionVisitPair(psaf_data)).T
plt.scatter(list(psaf_advisee_advisor_pair[0]), list(psaf_advisee_advisor_pair[1]), s=parameters['s'][2], 
            color='', edgecolors=parameters['colors'][0], marker='*', alpha=0.6, label='PSAF')


plt.xlabel("visit times of actions of partaker", font1)
plt.ylabel("visit times of actions of sharer", font1)
plt.title("The distribution of sharing for corresponding actions", font1)
plt.legend(loc=1, fontsize=14)

plt.savefig(save_fig_dir_name + key + "-state-action-visit.eps", bbox_inches = 'tight', format="eps")

plt.show()




