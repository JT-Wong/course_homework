# # -*- coding: utf-8 -*-
import copy
def contain(com_l, sum_com_l):

    i = 0
    while (i < len(sum_com_l)):
        e = sum_com_l[i]
        mark = False
        for j in e:
            if j not in com_l:
                mark = True
                break
        if not mark:
            return True
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

temp_l = [[],[],[],[],[]]


f = open('res_3.txt', 'r')
sum_l = []
lines = f.readlines()
i = 0
for line in lines:
    if i % 10000 == 0:
        print(i)
    i += 1

    if '[' in line:
        t = line.strip()[1:-1].replace(' ','').split(',')
    else:
        t = [line.strip()]
    if len(t) == 1:
        temp_l[0].append(t)
    elif len(t) == 2:
        if t not in temp_l[1]:
            temp_l[1].append(t)
    elif len(t) == 3:
        if t not in temp_l[2]:
         temp_l[2].append(t)
    elif len(t) == 4:
        if t not in temp_l[3]:
            temp_l[3].append(t)
    elif len(t) == 5:
        if t not in temp_l[4]:
            temp_l[4].append(t)

print(len(temp_l[0]))
print(len(temp_l[1]))
print(len(temp_l[2]))
print(len(temp_l[3]))
print(len(temp_l[4]))

f_w = open('res_f.txt', 'w+')
i = 0
for l in temp_l:
    for t in l :
        if i % 10000 == 0:
            print(i)
        i += 1
        if not contain(t, sum_l):
            sum_l.append(copy.deepcopy(t))
            for e in t:
                f_w.write(str(logic_table_list[int(e)]) + ';')
            f_w.write('\n')

f_w.close()

# f_w = open('res_8_new.txt', 'w+')
# for l in sum_l:
#     for i in l:
#         f_w.write(str(logic_table_list[int(i)]) + ' ')
#     f_w.write('\n')


