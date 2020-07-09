# coding=utf8


import argparse
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
sns.set(style="darkgrid")

import scipy as sp
import scipy.stats


def collect_experiment_data(source='/', runs=1, max_episode=5000, servers=1, agents=3,hfo=True,compact=False):
    # load all agent data
    evalGoalPercentages = defaultdict(list)
    evalGoalTimes = defaultdict(list)
    evalUsedBudgets = defaultdict(list)
    evalReward = defaultdict(list)
    evalSteps = defaultdict(list)
    evalTrials = np.array([])
    maxTrials = int(max_episode/20)+1

    goodRuns = 0
    for server in range(servers):
        for agent in range(1, agents+1):
            for run in range(0, runs):
                evalFile = os.path.join(source, "_"+ str(server) +"_"+ str(run+1) +"_AGENT_"+ str(agent) +"_RESULTS_eval")
                #print evalFile
                if os.path.isfile(evalFile):
                    if(hfo): #HFO experiment
                        try:
                            if compact:
                                _et, _egp, _egt, _eub = np.loadtxt(open(evalFile, "rb"), skiprows=1, delimiter=",", unpack=True)
                                _et, _egp, _egt, _eub = _et[:maxTrials], _egp[:maxTrials], _egt[:maxTrials], _eub[:maxTrials]
                            else:
                                _et, _egp, _egt, _eub, _er = np.loadtxt(open(evalFile, "rb"), skiprows=1, delimiter=",", unpack=True)
                                _et, _egp, _egt, _eub = _et[:maxTrials], _egp[:maxTrials], _egt[:maxTrials], _eub[:maxTrials]
                        except Exception as e:
                            print("agent:", agent, "now runs:", run)
                            print("collect_experiment_data:" ,e, evalFile)
                            continue
                        if sum(evalTrials)==0:   # store the right trial times
                            evalTrials = _et

                        # print("first?", sum(_et.shape), sum(evalTrials.shape))
                        if sum(_eub.shape) == sum(evalTrials.shape):
                            goodRuns += 1
                            for trial in _et:
                                evalGoalPercentages[(agent,trial)].append(_egp)
                                evalGoalTimes[(agent,trial)].append(_egt)
                                evalUsedBudgets[(agent,trial)].append(_eub)
                                if not compact:
                                    evalReward[(agent,trial)].append(_er)
                        else:
                            print("Error " + str(run+1) + " - "+ str(sum(_eub.shape))+" , "+str(sum(evalTrials.shape)))
                    else:
                        #try:
                        _et, _es, _eub = np.loadtxt(open(evalFile, "rb"), skiprows=1, delimiter=",", unpack=True)
                        #except:
                        #    continue
                        if sum(evalTrials)==0:
                            evalTrials = _et
                        #print(sum(_eub.shape), sum(evalTrials.shape))
                        if sum(_eub.shape) == sum(evalTrials.shape):
                            # print("runs:", run)
                            goodRuns += 1
                            for trial in _et:
                                evalSteps[(agent,trial)].append(_es)                                
                                evalUsedBudgets[(agent,trial)].append(_eub)
                        else:

                            print("Error " + str(run+1) + " - "+ str(sum(_eub.shape))+" , "+str(sum(evalTrials.shape)))
    goodRuns = int(goodRuns / agents)
    # print("source:", source)
    print('Could use %d runs from expected %d' % (goodRuns, runs))
 
    #print('len(evalGoalPercentages) %d --> %s %s' % (len(evalGoalPercentages), str(type(evalGoalPercentages[(1,20)])), str(evalGoalPercentages[(1,20)]) ))
    #print('len(evalGoalTimes) %d --> %s %s' % (len(evalGoalTimes), str(type(evalGoalTimes[(1,20)])), str(evalGoalTimes[(1,20)]) ))
    # print('len(evalUsedBudgets) %d --> %s %s' % (len(evalUsedBudgets), str(type(evalUsedBudgets[(1,20)])), str(len(evalUsedBudgets[(1,10)])) ))


    headerLine = []
    headerLine.append("Trial".encode())
    for run in range(1, runs+1):
        headerLine.append("Run"+str(run))

    if(hfo):
        with open(os.path.join(source, "__EVAL_goalpercentages"), 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow((headerLine))
            csvfile.flush()
            for i in range(sum(evalTrials.shape)):
                newrow = [evalTrials[i]]
                for j in evalGoalPercentages[(1,evalTrials[i])]:
                    newrow.append("{:.2f}".format(j[i]))
                csvwriter.writerow((newrow))
                csvfile.flush()
    
        with open(os.path.join(source, "__EVAL_goaltimes"), 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow((headerLine))
            csvfile.flush()
            for i in range(sum(evalTrials.shape)):
                newrow = [evalTrials[i]]
                for j in evalGoalTimes[(1,evalTrials[i])]:
                    newrow.append("{:.2f}".format(j[i]))
                csvwriter.writerow((newrow))
                csvfile.flush()
        if not compact:                
            with open(os.path.join(source, "__EVAL_reward"), 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow((headerLine))
                csvfile.flush()
                for i in range(sum(evalTrials.shape)):
                    newrow = [evalTrials[i]]
                    for j in evalReward[(1,evalTrials[i])]:
                        newrow.append("{:.2f}".format(j[i]))
                    csvwriter.writerow((newrow))
                    csvfile.flush()
    else:
        with open(os.path.join(source, "__EVAL_stepscaptured"), 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow((headerLine))
            csvfile.flush()
            for i in range(sum(evalTrials.shape)):
                newrow = [evalTrials[i]]
                for j in evalSteps[(1,evalTrials[i])]:
                    newrow.append("{:.2f}".format(j[i]))
                csvwriter.writerow((newrow))
                csvfile.flush()

    with open(os.path.join(source, "__EVAL_budgets"), 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow((headerLine))
        csvfile.flush()

        allBudgets = []
        for trial in range(sum(evalTrials.shape)):
            budgetAvg = [0]* (goodRuns)
            # print("goodruns:", goodRuns, "agents:", agents)
            for agent in range(1,agents+1):
                for i in range(len(evalUsedBudgets[(agent,evalTrials[trial])])):
                    #try:
                    # print(agent, len(evalUsedBudgets[(agent,evalTrials[trial])]))
                    budgetAvg[i] += evalUsedBudgets[(agent,evalTrials[trial])][i]/agents
                    #except:
                    #    print i, len(evalUsedBudgets[(agent,evalTrials[trial])])
            allBudgets.append(budgetAvg)
        for i in range(sum(evalTrials.shape)):
            newrow = [evalTrials[i]]
            #print allBudgets[i]
            for j in allBudgets[i]:
                #print(i,j[i])
                newrow.append("{:.2f}".format(j[i]))
            csvwriter.writerow((newrow))
            csvfile.flush()
    

def summarize_data(data, confidence=0.9):
    n = len(data)
    m = np.mean(data,axis=0)
    se = scipy.stats.sem(data,axis=0)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return np.asarray([m, m-h, m+h])


def summarize_experiment_data(source,hfo=True,compact=False):
    if hfo:    
        if compact:
            values = ["__EVAL_goalpercentages", "__EVAL_goaltimes", "__EVAL_budgets"]
        else:
            values = ["__EVAL_goalpercentages", "__EVAL_goaltimes", "__EVAL_budgets","__EVAL_reward"]
    else:
        values = ["__EVAL_stepscaptured", "__EVAL_budgets"]
    #values = ["__EVAL_goalpercentages", "__EVAL_goaltimes"]
    for value in values:
        evalFile = os.path.join(source, value)
        # print("evalFile:", evalFile)
        evalFileContent = np.loadtxt(open(evalFile, "rb"), skiprows=1, delimiter=",", unpack=True)

        # print("evalFileContent:", evalFileContent)
        trials = evalFileContent[0]
        data = evalFileContent[1:]
        update = summarize_data(data)
        headerLine = []
        headerLine.append("trial")
        headerLine.append("mean")
        headerLine.append("ci_down")
        headerLine.append("ci_up")

        value = value.replace("EVAL","SUMMARY")
        with open(os.path.join(source, value), 'w') as csvfile:
            csvwriter = csv.writer(csvfile)

            csvwriter.writerow((headerLine))
            csvfile.flush()

            for i in range(sum(trials.shape)):
                newrow = [trials[i]]
                for j in update.T[i]:
                    newrow.append("{:.2f}".format(j))
                csvwriter.writerow((newrow))
                csvfile.flush()
                
def cummulative_experiment_data(source,hfo=True,compact=False):
    if hfo:    
        if compact:
            values = ["__EVAL_goalpercentages", "__EVAL_goaltimes", "__EVAL_budgets"]
        else:
            values = ["__EVAL_goalpercentages", "__EVAL_goaltimes", "__EVAL_budgets","__EVAL_reward"]
    else:
        values = ["__EVAL_stepscaptured", "__EVAL_budgets"]
    #values = ["__EVAL_goalpercentages", "__EVAL_goaltimes"]
    for value in values:
        evalFile = os.path.join(source, value)
        #print(evalFile)
        evalFileContent = np.loadtxt(open(evalFile, "rb"), skiprows=1, delimiter=",", unpack=True)
        trials = evalFileContent[0]
        data = evalFileContent[1:]

        for rep in range(data.shape[0]):
            for index in range(1,data.shape[1]):
                data[rep][index] = data[rep][index-1] + data[rep][index]
        
        
        update = summarize_data(data)
        headerLine = []
        headerLine.append("trial")
        headerLine.append("mean")
        headerLine.append("ci_down")
        headerLine.append("ci_up")

        value = value.replace("EVAL","CUMMULATIVE")
        with open(os.path.join(source, value), 'w') as csvfile:
            csvwriter = csv.writer(csvfile)

            csvwriter.writerow((headerLine))
            csvfile.flush()

            for i in range(sum(trials.shape)):
                newrow = [trials[i]]
                for j in update.T[i]:
                    newrow.append("{:.2f}".format(j))
                csvwriter.writerow((newrow))
                csvfile.flush()


def draw_graph(source1 = None, name1 = "Algo1", significant1=None,
               source2 = None, name2 = "Algo2",significant2=None,
               source3 = None, name3 = "Algo3",significant3=None,
               source4 = None, name4 = "Algo4",significant4=None,
               source5 = None, name5 = "Algo5",significant5=None,
               source6 = None, name6 = "Algo5",significant6=None,
               what = "__SUMMARY_goalpercentages", ci = True,nCol = 1,
               #Parameters introduced to allow plot control
               xMin = None, xMax = None, yMin=None, yMax=None,bigFont=False, save_name=None, method_name=None, output_val=False
               ):

    plt.figure(figsize=(7,6), dpi=100)
    #Background
    plt.gca().set_facecolor('white')
    plt.grid(True,color='0.8')
    
    lineWidth = 6.0 if bigFont else 2.0

    if method_name:
        save_name_key = "HFO-"+method_name
    else:
        save_name_key = "HFO"

    data_list = []
    name_list = []

    if source1 != None:
        summary1File = os.path.join(source1, what)
        summary1Content = np.loadtxt(open(summary1File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X1 = summary1Content[0]
        Y11, Y12, Y13 = summary1Content[1],summary1Content[2],summary1Content[3]
        data_list.append(Y11)
        name_list.append(name1)
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X1, Y11, Y12, facecolor='#7570b3', alpha=0.2)
            plt.fill_between(X1, Y11, Y13, facecolor='#7570b3', alpha=0.2)
        if(not significant1 is None):
           plt.plot(X1,Y11,label=name1, color='#7570b3', linewidth=lineWidth,markevery=significant1,marker="d",markersize=3)
        else:
            # print(X1, Y11)
            plt.plot(X1, Y11, label=name1, color='#7570b3', linewidth=lineWidth, linestyle='-')
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])


    if source2 != None:
        summary2File = os.path.join(source2, what)
        summary2Content = np.loadtxt(open(summary2File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X2 = summary2Content[0]
        Y21, Y22, Y23 = summary2Content[1],summary2Content[2],summary2Content[3]
        data_list.append(Y21)
        name_list.append(name2)
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X2, Y21, Y22, facecolor='#e7298a', alpha=0.2)
            plt.fill_between(X2, Y21, Y23, facecolor='#e7298a', alpha=0.2)
        if(not significant2 is None):
            plt.plot(X2,Y21,label=name2, color='#e7298a', linewidth=lineWidth,markevery=significant2,marker="+",markersize=3)
        else:
            plt.plot(X2,Y21,label=name2, color='#e7298a', linewidth=lineWidth, linestyle='-.')
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])
    if source3 != None:
        summary3File = os.path.join(source3, what)
        summary3Content = np.loadtxt(open(summary3File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X3 = summary3Content[0]
        Y31, Y32, Y33 = summary3Content[1],summary3Content[2],summary3Content[3]
        data_list.append(Y31)
        name_list.append(name3)
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X3, Y31, Y32, facecolor='#66a61e', alpha=0.2)
            plt.fill_between(X3, Y31, Y33, facecolor='#66a61e', alpha=0.2)
        if(not significant3 is None):
            plt.plot(X3,Y31,label=name3, color='#66a61e', linewidth=lineWidth,marker="o",markevery=significant3,markersize=3)
        else:
            plt.plot(X3,Y31,label=name3, color='#66a61e', linewidth=lineWidth, linestyle=':')
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])
    if source4 != None:
        summary4File = os.path.join(source4, what)
        summary4Content = np.loadtxt(open(summary4File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X4 = summary4Content[0]
        Y41, Y42, Y43 = summary4Content[1],summary4Content[2],summary4Content[3]
        data_list.append(Y41)
        name_list.append(name4)
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X4, Y41, Y42, facecolor='#e6ab02', alpha=0.2)
            plt.fill_between(X4, Y41, Y43, facecolor='#e6ab02', alpha=0.2)
        if(not significant4 is None):
            plt.plot(X4,Y41,label=name4, color='#e6ab02', linewidth=lineWidth,markevery=significant4,marker="H",markersize=3)
        else:
            plt.plot(X4,Y41,label=name4, color='#e6ab02', linewidth=lineWidth, linestyle='--')
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])
    if source5 != None:
        summary5File = os.path.join(source5, what)
        summary5Content = np.loadtxt(open(summary5File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X5 = summary5Content[0]
        Y51, Y52, Y53 = summary5Content[1],summary5Content[2],summary5Content[3]
        data_list.append(Y51)
        name_list.append(name5)
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X5, Y51, Y52, facecolor='black', alpha=0.2)
            plt.fill_between(X5, Y51, Y53, facecolor='black', alpha=0.2)
        if(not significant5 is None):
            plt.plot(X5,Y51,label=name5, color='black', linewidth=lineWidth,markevery=significant5,marker="x",markersize=3)
        else:
            plt.plot(X5,Y51,label=name5, color='MediumPurple', linewidth=lineWidth)
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])
            
    if source6 != None:
        summary6File = os.path.join(source6, what)
        summary6Content = np.loadtxt(open(summary6File, "rb"), skiprows=1, delimiter=",", unpack=True)
        X6 = summary6Content[0]
        Y61, Y62, Y63 = summary6Content[1],summary6Content[2],summary6Content[3]
        data_list.append(Y61)
        name_list.append(name6)
        if what != "__SUMMARY_budgets" and ci:
            plt.fill_between(X6, Y61, Y62, facecolor='black', alpha=0.2)
            plt.fill_between(X6, Y61, Y63, facecolor='black', alpha=0.2)
        if(not significant6 is None):
            plt.plot(X6,Y61,label=name6, color='#999999', linewidth=lineWidth,markevery=significant6,marker="^",markersize=3)
        else:
            plt.plot(X6,Y61,label=name6, color='#999999', linewidth=lineWidth)
        if not yMin is None:
            plt.ylim([yMin,yMax])
        if not xMin is None:
            plt.xlim([xMin,xMax])
            
    axisSize = 25
    fontSize = 20

    if what == "__SUMMARY_goalpercentages":
        #plt.title('Goal Percentage per Trial')
        save_name_key += "-gp"
        plt.ylabel('Goal %', fontsize=fontSize, fontweight='bold')
    elif what == "__CUMMULATIVE_goalpercentages":
        #plt.title('Goal Percentage per Trial')
        save_name_key += "-cum-gp"
        plt.ylabel('Cummulative number of goals', fontsize=fontSize, fontweight='bold')
    elif what == "__SUMMARY_goaltimes":
        #plt.title('Average Frames to Goal per Trial')
        save_name_key += "-tg"
        plt.ylabel('Time to Goal', fontsize=fontSize, fontweight='bold')
    elif what == "__SUMMARY_budgets":
        #plt.title('Used Budget per Trial')
        save_name_key += "-budget"
        plt.ylabel('Budget', fontsize=fontSize, fontweight='bold')
    elif what == "__SUMMARY_stepscaptured":
        #plt.title('Used Budget per Trial')
        save_name_key += "-steps"
        plt.ylabel('Steps until captured', fontsize=fontSize, fontweight='bold')
    else:
        #plt.title('Unknown')
        save_name_key += "-unknown"
        plt.ylabel('Unknown')

    if not yMin is None:
        save_name_key += "-"+str(yMin)+"-"+str(yMax)
    if not xMin is None:
        plt.xlim([xMin, xMax])
        save_name_key += "-"+str(xMin)+"-"+str(xMax)

    plt.xlabel('Training Episodes', fontsize=fontSize, fontweight='bold')
    plt.legend(loc='best',prop={'size':fontSize, 'weight':'bold'},ncol=nCol,facecolor='white')
    plt.tick_params(axis='both', which='major', labelsize=axisSize)

    if save_name is not None:
        plt.tight_layout()
        plt.savefig(save_name+save_name_key+".eps", format="eps")
    else:
        pass
        # plt.show()

    if False and output_val:
        print("what:"+what)
        # print(data_list)
        # print(name_list)
        for index, name in enumerate(name_list):
            print("Name:"+name+"-Initial-Last-Average-AUC:"+str(data_list[index][0]) + "&" + str(data_list[index][-1]) + "&" +
                  str(round(np.mean(data_list[index]), 3)) +"&"+str(round(getAUC(data_list[index]), 3)))

def getAUC(data_list):
    begin = data_list[0]
    auc = 0
    for data in data_list[1:]:
        auc += np.trapz([begin, data])
        begin = data
    return auc


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--source',default='/home/ruben/playground/HFO/experiments/EVAL/2016_09_12-14.38.02_SARSA_1_5')
    parser.add_argument('-r','--runs',type=int, default=5)
    return parser.parse_args()

def main():
    parameter = get_args()
    #collect_experiment_data('/home/leno/gitProjects/AdHoc_AAMAS-17/ProcessedFiles/AdHocTD', 100,compact=True)
    #cummulative_experiment_data('/home/leno/gitProjects/AdHoc_AAMAS-17/ProcessedFiles/AdHocTD',compact=True)
    draw_graph(source1=parameter.source)
    draw_graph(source1=parameter.source, what="__SUMMARY_goaltimes")
    draw_graph(source1=parameter.source, what="__SUMMARY_budgets")

if __name__ == '__main__':
    main()