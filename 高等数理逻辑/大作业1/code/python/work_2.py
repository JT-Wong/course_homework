# -*- coding: utf-8 -*-
from python import com_set
import math
f = open('res_2.txt', 'w+')

# logic_table_list = [['1','00'],['1','01'],['1','10'],['1','11'],
#                     ['2', '0001'],['2', '0010'],['2', '0011'],
#                     ['2', '0100'],['2', '0101'],['2', '0110'],['2', '0111'],
#                     ['2', '1000'],['2', '1001'],['2', '1010'],['2', '1011'],
#                     ['2', '1100'],['2', '1101'],['2', '1110']]

logic_table_list = [['1','00'],['1','11'],
                    ['2', '0001'],['2', '0010'],['2', '0011'],
                    ['2', '0100'],['2', '0101'],['2', '0110'],['2', '0111'],
                    ['2', '1000'],['2', '1001'],['2', '1010'],['2', '1011'],
                    ['2', '1100'],['2', '1101'],['2', '1110']]

min_logic_list = []

for i in range(int(math.pow(2,len(logic_table_list)))):
    if i % 100 == 0:
        print(i)


    ele_str = bin(i)[2:]
    while len(ele_str) < len(logic_table_list):
        ele_str = '0' + ele_str

    if i == 49184:
        print(ele_str)

    mark_num = 0
    for min_logic in min_logic_list:
        for j in range(len(ele_str)):
            if int(ele_str[j]) < int(min_logic[j]):
                mark_num += 1
                break

    if mark_num == len(min_logic_list):
        inputs = {}
        k = 0
        for j in range(len(ele_str)):
            if ele_str[j] == '1':
                inputs['f' + str(k)] = logic_table_list[j]
                k += 1

        result = com_set.com_set_check(inputs)
        if result:
            mark = False
            for k in inputs:
                if inputs[k][0] == '2':
                    mark = True
            if mark == True:
                min_logic_list.append(ele_str)
                print(inputs)
                f.write(str(inputs) + '\n')

f.close()

# inputs={'f1':['1','00'],'f2':['1','11'],'f3':['2','1101'],}
# print(com_set.com_set_check(inputs))





