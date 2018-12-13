# -*- coding: utf-8 -*-
import com_set
import copy
import math
f = open('res_9.txt', 'w+')

# 寻找能够填补mark_1零位的mark_2
def combine_mark(mark_1, mark_2):
    mark = mark_1
    for i in range(len(mark_1)):
        if mark_1[i] == '0' and mark_2[i] == '1':
            mark = mark[:i] + '1' + mark[i+1:]
    return mark



# logic_table_list = [['0','0'],['0','1'],['1','00'],['1','01'],['1','10'],['1','11'],
#                     ['2','0000'],['2', '0001'],['2', '0010'],['2', '0011'],
#                     ['2', '0100'],['2', '0101'],['2', '0110'],['2', '0111'],
#                     ['2', '1000'],['2', '1001'],['2', '1010'],['2', '1011'],
#                     ['2', '1100'],['2', '1101'],['2', '1110'],['2','1111']]

logic_table_list = [['1','00'],['1','01'],['1','10'],['1','11'],
                    ['2', '0001'],['2', '0010'],['2', '0011'],
                    ['2', '0100'],['2', '0101'],['2', '0110'],['2', '0111'],
                    ['2', '1000'],['2', '1001'],['2', '1010'],['2', '1011'],
                    ['2', '1100'],['2', '1101'],['2', '1110']]


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
        f.write(str(i) + '\n')
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




count = 0
sum_com_l = []

def contain(com_l, sum_com_l):
    mark = False
    for i in com_l:
        if i > 3:
            mark = True
            break
    if not mark:
        return True

    for e in sum_com_l:
        mark = False
        if e == com_l:
            return True
        else:
            for i in e:
                if i not in com_l:
                    mark = True
                    break
            if not mark:
                return True

    return False


for T_0_e in T_0_list:
    print(count)


    com_l = []
    T_0_i = T_0_e[0]
    mark = logic_mark_list[T_0_i]
    com_l.append(T_0_i)
    count += 1

    for T_1_e in T_1_list:
        T_1_i = T_1_e[0]
        if T_1_i not in com_l:
            t_mark = logic_mark_list[T_1_i]
            new_mark = combine_mark(mark, t_mark)
            T_1_old_mark = mark
            if new_mark != mark:
                com_l.append(T_1_i)
                mark = new_mark
            if mark == '11111':
                com_l.sort()
                sum_com_l.append(copy.deepcopy(com_l))
                f.write(str(com_l) + '\n')
                com_l.remove(T_1_i)
                mark = T_1_old_mark
                continue

        for L_e in L_list:
            L_i = L_e[0]
            if L_i not in com_l:
                t_mark = logic_mark_list[L_i]
                new_mark = combine_mark(mark, t_mark)
                L_old_mark = mark
                if new_mark != mark:
                    com_l.append(L_i)
                    mark = new_mark
                if mark == '11111':
                    com_l.sort()
                    sum_com_l.append(copy.deepcopy(com_l))
                    f.write(str(com_l) + '\n')
                    com_l.remove(L_i)
                    mark = L_old_mark
                    continue

            for M_e in M_list:
                M_i = M_e[0]
                if M_i not in com_l:
                    t_mark = logic_mark_list[M_i]
                    new_mark = combine_mark(mark, t_mark)
                    M_old_mark = mark
                    if new_mark != mark:
                        com_l.append(M_i)
                        mark = new_mark
                    if mark == '11111':
                        com_l.sort()
                        sum_com_l.append(copy.deepcopy(com_l))
                        f.write(str(com_l) + '\n')
                        com_l.remove(M_i)
                        mark = M_old_mark
                        continue

                for S_e in S_list:
                    S_i = S_e[0]
                    if S_i not in com_l:
                        t_mark = logic_mark_list[S_i]
                        new_mark = combine_mark(mark, t_mark)
                        S_old_mark = mark
                        if new_mark != mark:
                            com_l.append(S_i)
                            mark = new_mark
                        if mark == '11111':
                            com_l.sort()
                            sum_com_l.append(copy.deepcopy(com_l))
                            f.write(str(com_l) + '\n')
                            com_l.remove(S_i)
                            mark = S_old_mark
                            continue

                    if (S_i != T_0_i) and (S_i != T_1_i) and (S_i != L_i) and (S_i != M_i) and S_i in com_l:
                        com_l.remove(S_i)
                        mark = S_old_mark

                if (M_i != T_0_i) and (M_i != T_1_i) and (M_i != L_i) and M_i in com_l:
                    com_l.remove(M_i)
                    mark = M_old_mark


            if (L_i != T_0_i) and (L_i != T_1_i) and L_i in com_l:
                com_l.remove(L_i)
                mark = L_old_mark


        if T_1_i != T_0_i and T_1_i in com_l:
            com_l.remove(T_1_i)
            mark = T_1_old_mark





# f.write(str(sum_com_l) +'\n')
# print(len(sum_com_l))

#
# f.write(str(T_0_list) + '\n')
# f.write(str(T_1_list) + '\n')
# f.write(str(L_list) + '\n')
# f.write(str(M_list) + '\n')
# f.write(str(S_list) + '\n')
# print(len(T_0_list))
# print(len(T_1_list))
# print(len(L_list))
# print(len(M_list))
# print(len(S_list))


