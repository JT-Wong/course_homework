# -*- coding: utf-8 -*-
from python import pro_logic
from python import com_set
import math
import sys

if __name__ == '__main__':
    num_logic_word = ['0', '1']
    basic_logic_word = ['¬', '∧', '∨', '⊕']
    derivation_word = ['→', '↔']


    f = open(file='data.txt', mode='r', encoding='utf8')
    lines = f.readlines()
    # 命题公式
    pro_logic_str = ''
    # 自定义逻辑联结词    {'f' : [2, 1101], }
    custom_logic_list = {}
    zero_ele_custom_logic_list = {}     # {'h' : 1/0}


    # 检查自定义逻辑联结词
    for line in lines:
        line = line.strip()
        if line == '' :
            continue
        elif '%' in line:
            line = line.split('%', 1)[0].strip()
            if line == '' :
                continue


        if '#' in line:
            line = line.split('#', 1)[1].strip()
            custom_logic_name, element_num, true_table = line.split(' ', 2)
            true_table = true_table.replace(' ', '')
            if custom_logic_name in custom_logic_list:
                print('exist custom logic ' + custom_logic_name)
                sys.exit(0)
            elif math.pow(2, int(element_num)) != len(true_table):
                print(custom_logic_name + ' define wrong')
                sys.exit(0)
            elif int(element_num) == 0:
                zero_ele_custom_logic_list[custom_logic_name] = int(true_table)
                continue
            else:
                custom_logic_list[custom_logic_name] = [element_num, true_table.replace(' ','')]
        else:
            pro_logic_str = line

    # 命题逻辑检测
    syntax_result = pro_logic.syntax_check(pro_logic_str, custom_logic_list, zero_ele_custom_logic_list)
    if syntax_result[0]:
        pro_logic_result = pro_logic.pro_logic_check(pro_logic_str, custom_logic_list, zero_ele_custom_logic_list, syntax_result[2])
        print(pro_logic_result)

    else:
        print(syntax_result[1])



    # 完全集检测
    # syntax_result = com_set.syntax_check(inputs)
    # if syntax_result[0]:
    #     com_set_result = com_set.com_set_check(custom_logic_list)
    #     print(com_set_result)
    # else:
    #     print(syntax_result[1])




