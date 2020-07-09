# -*- coding: gbk-*-

"""
analyse changes of Q values, and the max Q's action
"""
import os
import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt

temp_dir = {}
dir_path = "/home/cike/chauncy/coding/spyder/multiagent/soccerdata/actionvisit_20180507"


dir_files = os.listdir(dir_path)
for i in dir_files:
    if "AGENT_1" in i and "action" in i:
        file_path = os.path.join(dir_path, i)
        temp_dir = pkl.load(open(file_path, "rb"), encoding='iso-8859-1')



all_kyes = []
len_keys = []
zero_len_keys = []
for keys in temp_dir:
    values = np.array(temp_dir[keys], dtype=np.float32).T[:-1]
    values_len = len(values[values==np.float(0)])                  
                      
    all_kyes.append(keys)
    zero_len_keys.append(values_len)
    len_keys.append(len(temp_dir[keys]))

    
all_kyes = np.array(all_kyes)
len_keys = np.array(len_keys)
zero_len_keys = np.array(zero_len_keys)


max_keys_list = all_kyes[len_keys>2000]
zero_len_keys_list = zero_len_keys[len_keys>2000]


max_keys = tuple(list(max_keys_list[np.argmin(zero_len_keys_list)]))
max_len_keys_values = np.array(temp_dir[max_keys]).T[:-1]
label_index = np.array(temp_dir[max_keys]).T[-1]


# max_len = 30000
usableActions = ["SHOOT", "DRIBBLE", "PASSfar", "PASSnear", "MOVE"]
diffQ = []
maxQ = []
for index, i in enumerate(max_len_keys_values[:-1].T):
    diffQ.append(abs(max(i) - min(i)))
    maxQ.append(max(i))
    
    
plt.figure()
plt.plot(range(len(diffQ)), diffQ, label="diffQ")
plt.legend(loc='best')
plt.show()


plt.figure()
plt.plot(range(len(maxQ)), maxQ, label="maxQ")
plt.legend(loc='best')
plt.show()


diffQ = np.array(diffQ)
maxQ = np.array(maxQ)

plt.figure()
plt.plot(range(len(maxQ)), maxQ/(maxQ + 2), label="maxQ/ (maxQ/maxQ +2 )")
plt.legend(loc='best')
plt.show()
    

plt.figure()
for index, i in enumerate(max_len_keys_values[:-1]):
        plt.plot(range(len(i)), i, label=usableActions[index])

plt.legend(loc='best')
plt.show()
    


plt.figure()
plt.plot(range(len(max_len_keys_values[-1])), max_len_keys_values[-1], label=usableActions[index])
plt.legend(loc='best')
plt.show()



# maxQ - minQ
diffQ_list = []
diffQ_max_list = []
for key,value in temp_dir.items():
    value_array = np.array(value).T[:-1]
    diffQ = value_array.max(axis=0) - value_array.min(axis=0)
    diffQ_list.append(diffQ)
    diffQ_max_list.append(diffQ.max())
    
diffQ_max_list = np.array(diffQ_max_list)
len(diffQ_max_list[diffQ_max_list > 0.9])


def ask(visit):
    return np.power(1+0.5, -1*np.sqrt(visit))

def giveOne(visit):
    return 1 - np.power(1+1.5, -1*np.log2(visit))

def giveTwo(visit, diffQ):
    return 1 - np.power(1+1.5, -1*np.sqrt(visit)*diffQ)

def giveTwoOne(x):
    return 1 - np.power(1+0.05, -1*x)
 
def giveTHree(x):
    return x/(x+1)
    
# different visit
visit = 1000
plt.figure()
plt.plot(range(visit), ask(range(visit)), label="ask")
plt.plot(range(visit), giveOne(range(visit)), label="giveOne")
plt.plot(range(visit), giveTwo(range(visit), 0.5), label="giveTwo-diffQ 0.5")
plt.plot(range(visit), giveTwo(range(visit), 0.1), label="giveTwo-diffQ 0.1")
plt.legend(loc='best')
plt.show()  


# different diffQ
diffQ = 1
plt.figure()
plt.plot(np.arange(0, diffQ, 0.001), giveTwo(10, np.arange(0, diffQ, 0.001)), label="giveTwo-visit 10")
plt.plot(np.arange(0, diffQ, 0.001), giveTwo(50, np.arange(0, diffQ, 0.001)), label="giveTwo-visit 50")
plt.plot(np.arange(0, diffQ, 0.001), giveTwo(100, np.arange(0, diffQ, 0.001)), label="giveTwo-visit 100")
plt.plot(np.arange(0, diffQ, 0.001), giveTwo(1000, np.arange(0, diffQ, 0.001)), label="giveTwo-visit 100")
plt.legend(loc='best')
plt.show()  
    

# diffferent Q and visit
end = 100
plt.figure()
plt.plot(np.arange(0, end, 1), giveTwoOne(np.arange(0, end, 1)), label="giveTwoOne")
plt.show()  

        
# diffferent x/(x+1)
end = 1
plt.figure()
plt.plot(np.arange(0, end, 0.01), giveTHree(np.arange(0, end, 0.01)), label="giveTHree")
plt.show()    
   
    
    
    
    
    