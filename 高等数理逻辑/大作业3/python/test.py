# # -*- coding: utf-8 -*-
# import math
# # a = [1,2,3]
# # a.pop()
# # print(a)
#
#
# #
# # print(1 ^ 1)
# # print(0 ^ 0)
# # print(1 ^ 0)
# #
# # def Dec2Bin(dec):
# #     result = ''
# #
# #     if dec != 0:
# #         result = Dec2Bin(dec // 2)
# #         return result + str(dec % 2)
# #     else:
# #         return result
# #
# #
# # print(Dec2Bin(13))
# #
# # var_list = ['p', 'q', 'r']
# # true_table = {}
# # for var in var_list:
# #     true_table[var] = []
# #
# # var_num = len(var_list)
# # for i in range(int(math.pow(2, var_num))):
# #     true_table_str = bin(i)[2:]
# #     while len(true_table_str) < var_num:
# #         true_table_str = '0' + true_table_str
# #
# #     for j in range(var_num):
# #         true_table[var_list[j]].append(int(true_table_str[j]))
# #
# # for i in true_table:
# #     print(true_table[i])
# # a = 'p -> qpkdl -> q'
# # temp = '('
# # for i in range(len(a)):
# #     if a[i] == '-' and a[i+1] == '>':
# #         temp += ')' + a[i]
# #     elif a[i] == '>' and a[i-1] == '-':
# #         temp += a[i] + '('
# #     else:
# #         temp += a[i]
# # temp += ')'
# # print(temp)
#
# # ele_str = '0000'
# # j = 0
# # while j < len(ele_str):
# #     if ele_str[j] == '1':
# #         j += 1
# #     else:
# #         temp_ele_str = ele_str[:j] + '1' + ele_str[j+1:]
# #         print(temp_ele_str)
# #         print(int(temp_ele_str, 2))
# #         j += 1
#
# import math
# # print(int(math.pow(2,20)))
#
#
# # logic_table_list = [['1','00'],['1','01'],['1','10'],['1','11'],
# #                     ['2', '0001'],['2', '0010'],['2', '0011'],
# #                     ['2', '0100'],['2', '0101'],['2', '0110'],['2', '0111'],
# #                     ['2', '1000'],['2', '1001'],['2', '1010'],['2', '1011'],
# #                     ['2', '1100'],['2', '1101'],['2', '1110']]
# #
# # i = 1
# # while i < 255:
# #     ele_str = bin(i)[2:]
# #     while len(ele_str) < 8:
# #         ele_str = '0' + ele_str
# #     logic_table_list.append(['3', ele_str])
# #     i += 1
# #
# # print(logic_table_list)
#
# # print(72*72*198*180*184)
# import copy
# #
# # a =[2, 7]
# # b = [2, 7, 13]
# #
# # print(b[:len(a)] == a)
import copy
def contain(com_l, sum_com_l):
    if com_l in sum_com_l:
        return True

    i = 0
    while(i < len(sum_com_l)):
        e = sum_com_l[i]
        mark = False
        for j in com_l:
            if j not in e:
                mark = True
                break
        if not mark:
            del sum_com_l[i]
        else:
            i += 1

    return False
#
logic_table_list = [['0','0'],['0','1'],['1','00'],['1','01'],['1','10'],['1','11'],
                    ['2','0000'],['2', '0001'],['2', '0010'],['2', '0011'],
                    ['2', '0100'],['2', '0101'],['2', '0110'],['2', '0111'],
                    ['2', '1000'],['2', '1001'],['2', '1010'],['2', '1011'],
                    ['2', '1100'],['2', '1101'],['2', '1110'],['2','1111']]
i = 0
while i <= 255:
    ele_str = bin(i)[2:]
    while len(ele_str) < 8:
        ele_str = '0' + ele_str
    logic_table_list.append(['3', ele_str])
    i += 1



i = 0
f = open('res_5.txt', 'r')
sum_l = []
lines = f.readlines()
for line in lines:
    if '[' in line:
        t = line.strip()[1:-1].replace(' ','').split(',')
    else:
        t = [line.strip()]
    if not contain(t, sum_l):
        sum_l.append(copy.deepcopy(t))

f_w = open('res_6.txt', 'w+')
for l in sum_l:
    for i in l:
        f_w.write(str(logic_table_list[int(i)]) + ' ')
    f_w.write('\n')


