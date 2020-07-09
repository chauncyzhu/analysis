# coding=utf8
"""
三组数据有些许差别，需要分析一下，其中jingyun电脑的环境可能些许差别
"""
import evaluation as et

# version1, jingyun computer, 2017/12
version1 = "/home/cike/chauncy/game results/soccer game/old_data/agentData_version1"
# version2, mine computer, 2018/3
version2 = "/home/cike/chauncy/game results/soccer game/old_data//agentData_version2"
# version3, mine computer, 2018/3
version3 = "/home/cike/chauncy/game results/soccer game/old_data//agentData_version3"
# version4, version3's version1 and new HFO_2017
version4 = "/home/cike/chauncy/game results/soccer game/old_data//agentData_version4"
# version5 new experiments
version5 = "/home/cike/chauncy/game results/soccer game/old_data//agentData_version5"
# version6 using prob asking and comparing
version6 = "/home/cike/chauncy/game results/soccer game/old_data//agentData_version6"

# unlimited budget
dir_name = "/home/cike/chauncy/game results/soccer game/final_version/agentData_20190223/agentData_new"
# limited to 150
dir_name_one = "/home/cike/chauncy/game results/soccer game/final_version/agentData/agentData_150_new"
# limited to 50
dir_name_two = "/home/cike/chauncy/game results/soccer game/final_version/agentData/agentData_50_new"

limited = [True, True, True]


save_file_name = "/home/cike/桌面/"

# budget unlimited
if limited[0]:
    method_name = "unlimited"

    file_list = [dir_name+"/PartakerSharerTD-tg gp", dir_name+"/AdHocTD-tg gp", dir_name+"/AdhocTDQvalues", dir_name+"/SARSATile"]
    name_list = ['PSAF', "AdhocTD", "AdhocTD-Q", "Multi-IQL"]
    et.evaluation(file_list, name_list, 100, 10000, save_name=save_file_name, method_name=method_name)


# budget 150
if limited[1]:
    method_name = '150'
    file_list = [dir_name+"/PartakerSharerTD-tg gp", dir_name_one+"/AdHocTD", dir_name_one+"/AdhocTDQvalues", dir_name+"/SARSATile"]
    name_list = ['PSAF', "AdhocTD", "AdhocTD-Q", "Multi-IQL"]

    et.evaluation(file_list, name_list, 100, 10000, save_name=save_file_name, method_name=method_name)


# budget 50
if limited[2]:
    method_name = '50'
    file_list = [dir_name_two+"/PartakerSharerTD", dir_name_two+"/AdHocTD", dir_name_two+"/AdhocTDQvalues", dir_name+"/SARSATile"]
    name_list = ['PSAF', "AdhocTD", "AdhocTD-Q", "Multi-IQL"]

    et.evaluation(file_list, name_list, 100, 10000, save_name=save_file_name, method_name=method_name)


