# -*- coding: utf-8 -*-
import math
# a = [1,2,3]
# a.pop()
# print(a)


#
# print(1 ^ 1)
# print(0 ^ 0)
# print(1 ^ 0)
#
# def Dec2Bin(dec):
#     result = ''
#
#     if dec != 0:
#         result = Dec2Bin(dec // 2)
#         return result + str(dec % 2)
#     else:
#         return result
#
#
# print(Dec2Bin(13))
#
# var_list = ['p', 'q', 'r']
# true_table = {}
# for var in var_list:
#     true_table[var] = []
#
# var_num = len(var_list)
# for i in range(int(math.pow(2, var_num))):
#     true_table_str = bin(i)[2:]
#     while len(true_table_str) < var_num:
#         true_table_str = '0' + true_table_str
#
#     for j in range(var_num):
#         true_table[var_list[j]].append(int(true_table_str[j]))
#
# for i in true_table:
#     print(true_table[i])
# a = 'p -> qpkdl -> q'
# temp = '('
# for i in range(len(a)):
#     if a[i] == '-' and a[i+1] == '>':
#         temp += ')' + a[i]
#     elif a[i] == '>' and a[i-1] == '-':
#         temp += a[i] + '('
#     else:
#         temp += a[i]
# temp += ')'
# print(temp)

# ele_str = '0000'
# j = 0
# while j < len(ele_str):
#     if ele_str[j] == '1':
#         j += 1
#     else:
#         temp_ele_str = ele_str[:j] + '1' + ele_str[j+1:]
#         print(temp_ele_str)
#         print(int(temp_ele_str, 2))
#         j += 1

import math
print(int(math.pow(2,20)))