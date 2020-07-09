# coding=utf8
import os
import shutil

# dir_name = "/home/cike/chauncy/game results/soccer game/final_version/" \
           # "agentData_20190223/agentData_50_cp"
# dir_name = "/home/cike/chauncy/game results/new action reuse/hfo decay rate/20190702"

dir_name = "/media/cike/chauncy/agentData/"

# dir_name = ""


max_dir_index = 500
reindex = [43, 42, 46, 0, 0, 0]
max_res_length = 502

if dir_name[-1] == "/":
    dir_name_new = dir_name[:-1] + "_reindex" + "/"
else:
    dir_name_new = dir_name + "_reindex" + "/"
    dir_name = dir_name + "/"

if not os.path.exists(dir_name_new):
    os.mkdir(dir_name_new)

one_dir_list = os.listdir(dir_name)
print(one_dir_list)


def getOneResName(id):
    return [
        "_0_" + str(id) + "_AGENT_1_RESULTS_eval",
        "_0_" + str(id) + "_AGENT_1_RESULTS_train",
        "_0_" + str(id) + "_AGENT_2_RESULTS_eval",
        "_0_" + str(id) + "_AGENT_2_RESULTS_train",
        "_0_" + str(id) + "_AGENT_3_RESULTS_eval",
        "_0_" + str(id) + "_AGENT_3_RESULTS_train"
    ]


for index, i in enumerate(one_dir_list):
    file_list = os.listdir(os.path.join(dir_name, i))
    if file_list:
        # sort the file list
        file_list_sorted = file_list.sort()
        for j in range(max_dir_index):
            # the results of this id
            results_name_list = getOneResName(j)
            if set(file_list) > set(results_name_list):

                lines_one = len(open(os.path.join(dir_name, i, results_name_list[0]), 'rb').readlines())
                lines_two = len(open(os.path.join(dir_name, i, results_name_list[2]), 'rb').readlines())
                lines_three = len(open(os.path.join(dir_name, i, results_name_list[4]), 'rb').readlines())

                if lines_one == lines_two == lines_three == max_res_length:
                    new_dir_name = os.path.join(dir_name_new, i)
                    if not os.path.exists(new_dir_name):
                        os.mkdir(new_dir_name)

                    print(results_name_list, getOneResName(reindex[index]))
                    for name, new_name in zip(results_name_list, getOneResName(reindex[index])):
                        # print(reindex[index], name, new_name )
                        # print(os.path.join(dir_name, i, name), os.path.join(new_dir_name, new_name))
                        shutil.copy(os.path.join(dir_name, i, name), os.path.join(new_dir_name, new_name))
                    reindex[index] += 1









