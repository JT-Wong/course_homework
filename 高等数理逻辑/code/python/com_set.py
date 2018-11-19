# -*- coding: utf-8 -*-
import math

def T_0_check(last_true_table):
    result = True
    if int(last_true_table[0]) == 0:
        result = True
    else:
        result = False

    return result


def T_1_check(last_true_table):
    result = True
    if int(last_true_table[-1]) == 1:
        result = True
    else:
        result = False

    return result


# 计算真值表某行元素中1的个数
def cal_one_num(n):
    res = 0

    while(n != 0) :
        n = n - math.pow(2, int(math.log2(n)))
        res += 1

    return res

def L_check(last_true_table):
    result = True
    mark_1 = 0  # 1 : even  0 : odd
    mark_2 = 0  # 1 : odd  0 : even
    for i in range(len(last_true_table)):
        table_num = int(last_true_table[i])
        one_num = cal_one_num(i)
        if table_num == 1 :
            if one_num % 2 == 0:
                mark_1 += 1
            else:
                mark_2 += 1
        else:
            if one_num % 2 == 0:
                mark_2 += 1
            else:
                mark_1 += 1
    if mark_1 != len(last_true_table) and mark_2 != len(last_true_table):
        result = False
    return result


def M_check(ele_num, last_true_table):
    result = True

    for i in range(len(last_true_table)):
        table_num = int(last_true_table[i])
        if table_num == 0:
            continue
        # 1 不能指向 0
        else:
            ele_str = bin(i)[2:]
            while len(ele_str) < ele_num:
                ele_str = '0' + ele_str

            j = 0
            while j < len(ele_str):
                if ele_str[j] == '1':
                    j += 1
                else:
                    temp_ele_str = ele_str[:j] + '1' + ele_str[j+1:]
                    temp_table_num = int(last_true_table[int(temp_ele_str, 2)])
                    # 1 指向 0
                    if temp_table_num == 0 :
                        result = False
                        return result
                    j += 1

    return result


def S_check(last_true_table):
    result = True
    
    l = len(last_true_table)
    for i in range(int(l/2)):
        if int(last_true_table[i]) == int(last_true_table[l-1-i]):
            result = False
            break
        

    return result


# 自定义逻辑联结词    {'f' : [2, 1101], }
def com_set_check(custom_logic_list):
    result = False

    T_0_mark = False
    T_1_mark = False
    L_mark = False
    M_mark = False
    S_mark = False

    for logic_name in custom_logic_list:
        ele_num = int(custom_logic_list[logic_name][0])
        last_true_table = custom_logic_list[logic_name][1]
        if not T_0_mark:
            T_0_mark = not T_0_check(last_true_table)
        if not T_1_mark:
            T_1_mark = not T_1_check(last_true_table)
        if not L_mark:
            L_mark = not L_check(last_true_table)
        if not M_mark:
            M_mark = not M_check(ele_num, last_true_table)
        if not S_mark:
            S_mark = not S_check(last_true_table)


        if T_0_mark and T_1_mark and L_mark and M_mark and S_mark:
            result = True
            break

    return result




# c_l_1 = {'or' : ['2', '0111'], 'and' : ['2', '0001']}
# c_l_2 = {'or' : ['2', '0111'], 'not' : ['1', '10']}
# c_l_3 = {'nor' : ['2', '1000']}
# c_l_4 = {'f' : ['2', '0110'], 'g' : ['1', '10']}
# c_l_5 = {'f' : ['2', '0110'], 'g' : ['2', '0111'], 'h' : ['2', '0001']}
# c_l_6 = {'f' : ['2', '0001'], 'g' : ['2', '1001'], 'h' : ['2', '0110']}
# c_l_7 = {'f' : ['2', '0111'], 'g' : ['2', '1001'], 'h' : ['1', '00']}
# c_l_8 = {'f' : ['2', '0111'], 'g' : ['2', '0001'], 'h' : ['2', '1101'], 'i' : ['2', '1001']}

# c_l_1 = {'f1' : ['0', '1'], 'f2' : ['1', '10']}
# res = com_set_check(c_l_1)
# print(res)
#
# res = com_set_check(c_l_2)
# print(res)
#
# res = com_set_check(c_l_3)
# print(res)
#
# res = com_set_check(c_l_4)
# print(res)
#
# res = com_set_check(c_l_5)
# print(res)
#
# res = com_set_check(c_l_6)
# print(res)
#
# res = com_set_check(c_l_7)
# print(res)
#
# res = com_set_check(c_l_8)
# print(res)


"""
# or 2 0111
# and 2 0001
# not 1 10

# f 2 0110
# g 1 10

# f 2 0110
# g 2 0111
# h 2 0001

# f 2 0001
# g 2 1001
# h 2 0110

# f 2 0111
# g 2 1001
# h 1 00


"""