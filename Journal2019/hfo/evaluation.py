# coding=utf8
import exp_utils as exp_utils


def evaluation(source_list, name_list, max_run, max_episode, save_name=None, method_name=None, budget_only=False):
    source_list = source_list + [None]*(6-len(source_list))
    name_list = name_list + [None]*(6-len(name_list))

    source1, source2, source3, source4, source5,source6 = source_list[0], source_list[1], source_list[2], source_list[3], source_list[4], source_list[5]
    name1, name2, name3, name4, name5, name6 = name_list[0], name_list[1], name_list[2], name_list[3], name_list[4], name_list[5]

    # source1 = fileFolder + 'SARSATile'    # 37 runs, actually 38 runs
    # source2 = fileFolder + 'AdHocTD'    # 49 runs, actually 50 runs
    # source3 = fileFolder + 'AdhocTD_new'     # 47 runs
    # source4 = fileFolder + 'AdhocAbsorbActionVisit'     # 26 runs
    # source5 = fileFolder + 'actionvisit'    # 14 runs
    # source6 = fileFolder + 'AdhocAbsorbMaxReplace_NoEdit'    # 22 runs
    #
    #
    # name1 = 'SARSATile'
    # name2 = 'AdHocTD'
    # name3 = 'AdhocTD_new'
    # name4 = 'AdhocAbsorbActionVisit'
    # name5 = 'actionvisit'
    # name6 = 'AdhocAbsorbMaxReplace_NoEdit'    # 24 runs

    if source1 != None:
        #Prepare intermediary files with experiment's summary.
        exp_utils.collect_experiment_data(source1, runs=max_run, max_episode=max_episode)
        #summarize data of multi runs: means and confidence
        exp_utils.summarize_experiment_data(source1)
        #cummulative data of multi runs: the previous data will be added to the current data
        exp_utils.cummulative_experiment_data(source1)

    if source2 != None:
        exp_utils.collect_experiment_data(source2, runs=max_run, max_episode=max_episode)
        exp_utils.summarize_experiment_data(source2)
        exp_utils.cummulative_experiment_data(source2)

    if source3 != None:
        exp_utils.collect_experiment_data(source3, runs=max_run, max_episode=max_episode)
        exp_utils.summarize_experiment_data(source3)
        exp_utils.cummulative_experiment_data(source3)

    if source4 != None:
        exp_utils.collect_experiment_data(source4, runs=max_run, max_episode=max_episode)
        exp_utils.summarize_experiment_data(source4)
        exp_utils.cummulative_experiment_data(source4)

    if source5 != None:
        exp_utils.collect_experiment_data(source5, runs=max_run, max_episode=max_episode)
        exp_utils.summarize_experiment_data(source5)
        exp_utils.cummulative_experiment_data(source5)

    if source6 != None:
        exp_utils.collect_experiment_data(source6, runs=max_run, max_episode=max_episode)
        exp_utils.summarize_experiment_data(source6)
        exp_utils.cummulative_experiment_data(source6)

    #Intervals for zoomed averages
    xMinPerc = max_episode-3000
    xMaxPerc = max_episode

    if max_episode < 5000:
        yMinPerc = 50
        yMaxPerc = 75
    else:
        yMinPerc = 62
        yMaxPerc = 90


    #Intervals for Time for Goal graphs
    xMinStep = max_episode-3000
    xMaxStep = max_episode
    if max_episode < 5000:
        yMinStep = 90
        yMaxStep = 115
    else:
        yMinStep = 85
        yMaxStep = 120

    xMinStep2 = 0
    xMaxStep2 = max_episode
    yMinStep2 = 30
    yMaxStep2 = 110

    printCI = True

    if not budget_only:
        exp_utils.draw_graph(source1=source1,name1=name1,source2=source2,name2=name2,source3=source3,name3=name3, name4=name4,source4=source4, source5=source5, name5=name5, source6=source6, name6=name6, ci=printCI,
                             save_name=save_name, nCol=2, method_name=method_name, output_val=True)

        exp_utils.draw_graph(source1=source1,name1=name1, source2=source2,name2=name2,source3=source3,name3=name3, source4=source4, name4=name4, source5=source5, name5=name5, source6=source6, name6=name6, xMin = xMinPerc, xMax = xMaxPerc, yMin = yMinPerc,
                             yMax = yMaxPerc, ci=False,nCol=2, save_name=save_name, method_name=method_name)

        exp_utils.draw_graph(source1=source1,name1=name1, source2=source2,name2=name2,source3=source3,name3=name3, source4=source4, name4=name4, source5=source5, name5=name5, source6=source6, name6=name6, what="__SUMMARY_goaltimes",ci=printCI,
                            xMin = xMinStep2, xMax = xMaxStep2, yMin = yMinStep2, yMax = yMaxStep2, nCol=2, save_name=save_name, method_name=method_name, output_val=True)

        exp_utils.draw_graph(source1=source1, name1=name1, source2=source2,name2=name2,source3=source3,name3=name3, source4=source4, name4=name4, source5=source5, name5=name5, source6=source6, name6=name6, what="__SUMMARY_goaltimes",
                            xMin = xMinStep, xMax = xMaxStep, yMin = yMinStep, yMax = yMaxStep, ci=False, nCol=2, save_name=save_name, method_name=method_name)

    if "Multi-IQL" == name4:
        name4 = None
        source4 = None
    
    exp_utils.draw_graph(source1=source1,name1=name1, source2=source2,name2=name2,source3=source3,name3=name3, source4=source4, name4=name4, source5=source5, name5=name5, source6=source6, name6=name6, what="__SUMMARY_budgets",ci=printCI,nCol=1, save_name=save_name, method_name=method_name)


