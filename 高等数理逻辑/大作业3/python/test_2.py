# -*- coding: utf-8 -*-
from python import com_set
import copy
import math

# 寻找能够填补mark_1零位的mark_2
def combine_mark(mark_1, mark_2):
    mark = mark_1
    for i in range(len(mark_1)):
        if mark_1[i] == '0' and mark_2[i] == '1':
            mark = mark[:i] + '1' + mark[i+1:]
    return mark



logic_table_list = [['1','00'],['1','01'],['1','10'],['1','11'],
                    ['2', '0001'],['2', '0010'],['2', '0011'],
                    ['2', '0100'],['2', '0101'],['2', '0110'],['2', '0111'],
                    ['2', '1000'],['2', '1001'],['2', '1010'],['2', '1011'],
                    ['2', '1100'],['2', '1101'],['2', '1110']]

# logic_table_list = [['1','00'],['1','11'],
#                     ['2', '0001'],['2', '0010'],['2', '0011'],
#                     ['2', '0100'],['2', '0101'],['2', '0110'],['2', '0111'],
#                     ['2', '1000'],['2', '1001'],['2', '1010'],['2', '1011'],
#                     ['2', '1100'],['2', '1101'],['2', '1110']]


# logic_table_list = [['1','00'],['1','11']]
#
i = 1
while i < 255:
    ele_str = bin(i)[2:]
    while len(ele_str) < 8:
        ele_str = '0' + ele_str
    logic_table_list.append(['3', ele_str])
    i += 1

T_0_list = {}
T_1_list = {}
L_list = {}
M_list = {}
S_list = {}

logic_mark_list = {}
logic_mark_num_list = {}

for i in range(len(logic_table_list)):
    T_0_mark = not com_set.T_0_check(logic_table_list[i][1])
    T_1_mark = not com_set.T_1_check(logic_table_list[i][1])
    L_mark = not com_set.L_check(logic_table_list[i][1])
    M_mark = not com_set.M_check(int(logic_table_list[i][0]), logic_table_list[i][1])
    S_mark = not com_set.S_check(logic_table_list[i][1])

    if T_0_mark and T_1_mark and L_mark and M_mark and S_mark:
        continue

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

# logic_mark_num_list = sorted(logic_mark_num_list.items(),key = lambda x:x[1],reverse = True)
for i in T_0_list:
    T_0_list[i] = logic_mark_num_list[i]
for i in T_1_list:
    T_1_list[i] = logic_mark_num_list[i]
for i in L_list:
    L_list[i] = logic_mark_num_list[i]
for i in M_list:
    M_list[i] = logic_mark_num_list[i]
for i in S_list:
    S_list[i] = logic_mark_num_list[i]


T_0_list = sorted(T_0_list.items(),key = lambda x:x[1],reverse = True)
T_1_list = sorted(T_1_list.items(),key = lambda x:x[1],reverse = True)
L_list = sorted(L_list.items(),key = lambda x:x[1],reverse = True)
M_list = sorted(M_list.items(),key = lambda x:x[1],reverse = True)
S_list = sorted(S_list.items(),key = lambda x:x[1],reverse = True)
print(T_0_list)
print(T_1_list)
print(L_list)
print(M_list)
print(S_list)