# -*- coding: utf-8 -*-
import com_set
import copy
import math

#
# logic_table_list = [['0','1'],['0','0'],
#                     ['1','11'],['1','10'],['1','01'],['1','00'],
#                     ['2', '1111'],['2','1110'],['2','1101'],['2','1100'],
# ['2', '1011'],['2', '1010'],['2', '1001'],['2', '1000'],
# ['2', '0111'],['2', '0110'],['2', '0101'],['2', '0100'],
# ['2', '0011'],['2', '0010'],['2', '0001'],['2','0000'],
# ]
#
#
# i = 255
# while i >= 0:
#     ele_str = bin(i)[2:]
#     while len(ele_str) < 8:
#         ele_str = '0' + ele_str
#     logic_table_list.append(['3', ele_str])
#     i -= 1
logic_table_list = [['3', '00111100'], ['3','11110000']]
#logic_table_list = [['3', '00000000'],['3', '01101001'],['3', '01111111'],['3', '11111111']]

T_0_list = {}
T_1_list = {}
L_list = {}
M_list = {}
S_list = {}

logic_mark_list = {}
logic_mark_num_list = {}

for i in range(len(logic_table_list)):
    if '1' not in logic_table_list[i][1] :
        T_0_mark,T_1_mark,L_mark,M_mark,S_mark = False,True,False,False,True
    elif '0' not in logic_table_list[i][1] :
        T_0_mark,T_1_mark,L_mark,M_mark,S_mark = True,False,False,False,True
    else:
        T_0_mark = not com_set.T_0_check(logic_table_list[i][1])
        T_1_mark = not com_set.T_1_check(logic_table_list[i][1])
        L_mark = not com_set.L_check(int(logic_table_list[i][0]), logic_table_list[i][1])
        M_mark = not com_set.M_check(int(logic_table_list[i][0]), logic_table_list[i][1])
        S_mark = not com_set.S_check(logic_table_list[i][1])

    # if T_0_mark and T_1_mark and L_mark and M_mark and S_mark:
    #     continue

    if i not in logic_mark_list:
        logic_mark_list[i] = '00000'
        logic_mark_num_list[i] = 0

    if T_0_mark:
        logic_mark_list[i] = '1' + logic_mark_list[i][1:]
        logic_mark_num_list[i] += 1

        if i not in T_0_list:
            T_0_list[i] = 0

    if T_1_mark:
        logic_mark_list[i] = logic_mark_list[i][0] + '1' + logic_mark_list[i][2:]
        logic_mark_num_list[i] += 1
        if i not in T_1_list:
            T_1_list[i] = 0
    if L_mark:
        logic_mark_list[i] = logic_mark_list[i][0:2] + '1' + logic_mark_list[i][3:]
        logic_mark_num_list[i] += 1
        if i not in L_list:
            L_list[i] = 0
    if M_mark:
        logic_mark_list[i] = logic_mark_list[i][0:3] + '1' + logic_mark_list[i][4:]
        logic_mark_num_list[i] += 1
        if i not in M_list:
            M_list[i] = 0
    if S_mark:
        logic_mark_list[i] = logic_mark_list[i][0:4] + '1'
        logic_mark_num_list[i] += 1
        if i not in S_list:
            S_list[i] = 0

f = open('type.txt', 'w+')
for i in logic_mark_list:
    f.write(logic_mark_list[i]+'\n')