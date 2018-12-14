# # -*- coding: utf-8 -*-
import math

# f1 = open('res_f.txt', 'r')
# f2 = open('res_f_2.txt', 'w+')
#
# lines = f1.readlines()
# for line in lines:
#     str_l = line.strip().split(';')
#     r = ''
#     for s in str_l:
#         if s.strip() == '':
#             continue
#         n,t = s.replace("'",'').replace('[','').replace(']','').replace(' ','').split(',')
#         if n == '0':
#             r += 'A'
#         elif n == '1':
#             r += 'B'
#         elif n == '2':
#             r += 'C'
#         elif n == '3':
#             r += 'D'
#         r += str(int(t, 2)) + '\t'
#     f2.write(r + '\n')





def contain(e_1, l_2):
    for e_2 in l_2:
        mark = False
        for j in e_2:
            if j not in e_1:
                mark = True
                break
        if (not mark) and len(e_1) == len(e_2):
            return True
    return False


f1 = open('res_f_2.txt', 'r')
f2 = open('result.txt', 'r')

l_1 = []
lines = f1.readlines()
for line in lines:
    l_1.append(line.strip().split('\t'))

l_2 = []
lines = f2.readlines()
for line in lines:
    l_2.append(line.strip().split('\t'))

for e_1 in l_1:
    if not contain(e_1, l_2):
        print(e_1)
