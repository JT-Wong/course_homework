# -*- coding: utf-8 -*-
import math
import traceback
import sys

def arg_check(pro_logic, i):
    temp = ''
    while i < len(pro_logic):
        if pro_logic[i].isalpha() or pro_logic[i].isdigit():
            temp += pro_logic[i]
            i += 1
        else:
            break
    return [i - 1, temp]



def syntax_check(pro_logic, custom_logic_list, zero_ele_custom_logic_list):
    num_logic_word = ['0', '1']
    basic_logic_word = ['¬', '∧', '∨', '⊕']
    derivation_word = ['→', '↔']
    # 语法检测结果 错误说明 变元列表
    result = [True, 'no error', []]


    # 检测推导符两边情况
    temp_num = pro_logic.count('→')
    temp_str = pro_logic.split('→', temp_num)
    for s in temp_str:
        if s.strip() == '':
            result = [False, "→ left or right cnt't be null", []]
            return result
    temp_num = pro_logic.count('↔')
    temp_str = pro_logic.split('↔', temp_num)
    for s in temp_str:
        if s.strip() == '':
            result = [False, " ↔ left or right cnt't be null", []]
            return result

    i = 0
    # 状态
    state = 0
    '''
    0 : begin  (  → ↔     
    1 : 0 1
    2 : 命题变元 )  custome_end
    3 : ¬
    4 : ∧ ∨ ⊕
    5 : custome_begin 
    
    '''
    # 括号栈
    bracket_stack = []
    # 判断是否还在custom内,括号全匹配上
    custom_stack = 0

    try:
        while i < len(pro_logic):
            if state == 0 or state == 3 or state == 4:
                if  pro_logic[i] == ' ':
                    pass
                elif pro_logic[i] == '0' or pro_logic[i] == '1':
                    state = 1
                elif pro_logic[i].isalpha():
                    arg_result = arg_check(pro_logic, i)
                    # 更新下标
                    i = arg_result[0]
                    # 添加变元
                    arg_name = arg_result[1]
                    # 普通命题变元
                    if arg_name not in custom_logic_list:
                        if arg_name not in result[2] and arg_name not in zero_ele_custom_logic_list:
                            result[2].append(arg_name)
                        state = 2
                    # 自定义逻辑联结词
                    else:
                        state = 5


                elif pro_logic[i] == '¬':
                    state = 3
                elif pro_logic[i] == '(':
                    # 记录当且状态
                    bracket_stack.append(state)
                    state = 0
                    if custom_stack > 0 :
                        custom_stack += 1

                else:
                    result = [False, 'error in ' + pro_logic[i - 1:i + 1], []]
                    break
                i += 1


            elif state == 1 or state == 2:
                if  pro_logic[i] == ' ':
                    pass
                elif pro_logic[i] == '∧' or pro_logic[i] == '∨' or pro_logic[i] == '⊕':
                    state = 4
                elif pro_logic[i] == '→' or pro_logic[i] == '↔':
                    state = 0
                elif pro_logic[i] == ')':
                    bracket_stack.pop()
                    if custom_stack > 0 :
                        custom_stack -= 1
                elif pro_logic[i] == ',' and custom_stack > 0:
                    state = 0
                else:
                    result = [False, 'error in ' + pro_logic[i - 1:i + 1], []]
                    break
                i += 1

            elif state == 5:
                if pro_logic[i] == '(':
                    bracket_stack.append(state)
                    custom_stack += 1
                    state = 0
                else:
                    result = [False, 'error in ' + pro_logic[i - 1:i + 1], []]
                    break

                i += 1

            else:
                print('error state')
                result = [False, 'error in ' + pro_logic[i-1:i+1], []]
                break
    except:
        result = [False, 'error in ' + pro_logic[i - 1:i + 1], []]


    if result[0] == True :
        if len(bracket_stack) != 0:
            result = [False, 'lost )', []]

        if state == 0 or state == 1 or state == 2 :
            pass
        else:
            result = [False, 'proposition not complete', []]


    return result


# 基本逻辑联结词的计算
def basic_logic_calculate(arg1, arg2, op):
    result = 0
    if op == '∧':
        result = int(arg1) and int(arg2)
    elif op == '∨':
        result = int(arg1) or int(arg2)
    elif op == '⊕':
        result = int(arg1) ^ int(arg2)
    elif op == '→':
        if int(arg1) == 1 and int(arg2) == 0:
            result = 0
        else:
            result = 1
    elif op == '↔':
        if int(arg1) == int(arg2):
            result = 1
        else:
            result = 0
    return result



# 自定义逻辑联结词的计算
def custom_logic_calculate(custom_logic_word, pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, begin_index):
    end_index = len(pro_logic) - 1
    result = [0, end_index]

    arg_value_list = []

    # 括号栈
    bracket_stack = 0
    i = begin_index
    if pro_logic[i] == '(':
        bracket_stack += 1
        i += 1
    else:
        print('lost ( after ' + str(custom_logic_word))
        sys.exit(0)

    element_num = 0

    element = ''
    while i < len(pro_logic):
        if pro_logic[i] == ' ':
            pass
        elif pro_logic[i] == '(':
            bracket_stack += 1
            element += pro_logic[i]
        elif pro_logic[i] == ')':
            bracket_stack -= 1
            element += pro_logic[i]
        # 收集到自定义逻辑联结词的一个完整命题变元
        elif pro_logic[i] == ',' and bracket_stack == 1:
            temp_result = formula_calculate(element, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, 0, False)
            if temp_result[0] == 0 or temp_result[0] == 1:
                arg_value_list.append(temp_result[0])
            else:
                arg_value_list.append(0)
            element = ''
            element_num += 1
        else:
            element += pro_logic[i]

        # 整个自定义的逻辑联结词结束
        if bracket_stack <= 0:
            if element[-1] == ')':
                element = element[:-1]

            temp_result = formula_calculate(element, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, 0, False)
            if temp_result[0] == 0 or temp_result[0] == 1:
                arg_value_list.append(temp_result[0])
            else:
                arg_value_list.append(0)
            element = ''
            element_num += 1

            result[1] = i
            break

        i += 1


    if element_num != int(custom_logic_list[custom_logic_word][0]):
        print(custom_logic_word + ' element num is not right')
        sys.exit(0)

    arg_value_str = ''
    for arg_value in arg_value_list:
        arg_value_str += str(arg_value)

    result[0] = int(custom_logic_list[custom_logic_word][1][int(arg_value_str,2)])
    return result


# 对左右两侧的命题进行计算
# 出现¬和(时进行递归运算
def formula_calculate(pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, begin_index, not_mark):
    end_index = len(pro_logic) - 1
    result = [0, end_index]     #end_index 已分析的下标
    arg_1 = -1
    arg_2 = -1
    if not_mark:
        op = '¬'
    else:
        op = ''

    i = begin_index
    try:
        while i < len(pro_logic):
            if pro_logic[i] == ' ':
                pass
            elif pro_logic[i] == '0' or pro_logic[i] == '1':
                if op == '':
                    if arg_1 == -1:
                        arg_1 = int(pro_logic[i])
                    else:
                        print('error in ' + pro_logic[i-1:i+1])
                        sys.exit(0)
                # 正确处理后要返回
                elif op == '¬':
                    if arg_1 == -1:
                        arg_1 = 1 ^ int(pro_logic[i])
                        result[0] = arg_1
                        result[1] = i
                        return result
                    else:
                        print('error in ' + pro_logic[i - 1:i + 1])
                        sys.exit(0)
                else:
                    if arg_1 == -1:
                        print('error in ' + pro_logic[i - 1:i + 1])
                        sys.exit(0)
                    else:
                        arg_1 = basic_logic_calculate(arg_1, pro_logic[i], op)
                        op = ''


            elif pro_logic[i].isalpha():
                arg_result = arg_check(pro_logic, i)
                i = arg_result[0]
                arg_name = arg_result[1]

                # 自定义逻辑联结词
                if arg_name in custom_logic_list:
                    temp_result = custom_logic_calculate(arg_name, pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, i + 1)
                    arg_value = temp_result[0]
                    i = temp_result[1]
                elif arg_name in zero_ele_custom_logic_list:
                    arg_value = zero_ele_custom_logic_list[arg_name]
                else:
                    arg_value = true_table[arg_name][true_table_id]

                if op == '':
                    if arg_1 == -1:
                        arg_1 = int(arg_value)
                    else:
                        print('error in ' + pro_logic[i - 1:i + 1])
                        sys.exit(0)
                elif op == '¬':
                    if arg_1 == -1:
                        arg_1 = 1 ^ int(arg_value)
                        result[0] = arg_1
                        result[1] = i
                        return result
                    else:
                        print('error in ' + pro_logic[i - 1:i + 1])
                        sys.exit(0)
                else:
                    if arg_1 == -1:
                        print('error in ' + pro_logic[i - 1:i + 1])
                        sys.exit(0)
                    else:
                        arg_1 = basic_logic_calculate(arg_1, arg_value, op)
                        op = ''


            elif pro_logic[i] == '∧' or pro_logic[i] == '∨' or pro_logic[i] == '⊕':
                if op == '' :
                    op = pro_logic[i]
                else:
                    result[0] = -1
                    return result
            elif pro_logic[i] == '→' or pro_logic[i] == '↔':
                if op == '' :
                    op = pro_logic[i]
                else:
                    print('error in ' + pro_logic[i - 1:i + 1])
                    sys.exit(0)

            elif pro_logic[i] == '¬':
                temp_result = formula_calculate(pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, i+1, True)
                arg_value = int(temp_result[0])
                i = temp_result[1]

                if op == '':
                    if arg_1 == -1:
                        arg_1 = int(arg_value)
                    else:
                        print('error in ' + pro_logic[i - 1:i + 1])
                        sys.exit(0)
                elif op == '¬':
                    if arg_1 == -1:
                        arg_1 = 1 ^ int(arg_value)
                        result[0] = arg_1
                        result[1] = i
                        return result
                    else:
                        print('error in ' + pro_logic[i - 1:i + 1])
                        sys.exit(0)
                else:
                    if arg_1 == -1:
                        print('error in ' + pro_logic[i - 1:i + 1])
                        sys.exit(0)
                    else:
                        arg_1 = basic_logic_calculate(arg_1, arg_value, op)
                        op = ''
            elif pro_logic[i] == '(':
                temp_result = formula_calculate(pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, i+1, False)
                arg_value = temp_result[0]
                i = temp_result[1]

                if op == '':
                    if arg_1 == -1:
                        arg_1 = int(arg_value)
                    else:
                        print('error in ' + pro_logic[i - 1:i + 1])
                        sys.exit(0)
                elif op == '¬':
                    if arg_1 == -1:
                        arg_1 = 1 ^ int(arg_value)
                        result[0] = arg_1
                        result[1] = i
                        return result
                    else:
                        print('error in ' + pro_logic[i - 1:i + 1])
                        sys.exit(0)
                else:
                    if arg_1 == -1:
                        print('error in ' + pro_logic[i - 1:i + 1])
                        sys.exit(0)
                    else:
                        arg_1 = basic_logic_calculate(arg_1, arg_value, op)
                        op = ''

            elif pro_logic[i] == ')':
                if arg_1 == -1:
                    print('error in ' + pro_logic[i - 1:i + 1])
                    sys.exit(0)
                else:
                    result[0] = arg_1
                    result[1] = i
                    return result
            else:
                print('error in ' + pro_logic[i - 1:i + 1])
                sys.exit(0)

            i += 1

    except Exception as e:
        traceback.print_exc()

    result[0] = arg_1
    return result



def pro_logic_check(pro_logic, custom_logic_list, zero_ele_custom_logic_list, var_list):
    result = 'always true / always false / true status : '

    # 命题逻辑成立时的真值表列数
    true_states = []

    true_table = {}
    for var in var_list:
        true_table[var] = []

    # 生成真值表
    var_num = len(var_list)
    for i in range(int(math.pow(2, var_num))):
        true_table_str = bin(i)[2:]
        while len(true_table_str) < var_num:
            true_table_str = '0' + true_table_str

        for j in range(var_num):
            true_table[var_list[j]].append(int(true_table_str[j]))

    # 以→和↔切分命题公式
    temp = '(' + pro_logic + ')'
    i = 0
    while i < len(temp):

        if temp[i] == '→' or temp[i] == '↔':
            # 填充右边的括号
            j = i + 1
            bracket_stack = 0
            while j < len(temp):
                if temp[j] == '(':
                    bracket_stack += 1
                elif temp[j] == ')':
                    bracket_stack -= 1
                    if bracket_stack < 0:
                        temp = temp[:j] + ')' + temp[j:]
                        break
                elif temp[j] == '→' or temp[j] == '↔':
                    temp = temp[:j] + ')' + temp[j:]
                    break
                else:
                    pass
                j += 1
            temp = temp[:i+1] + '(' + temp[i+1:]

            # 填充左边的括号
            j = i - 1
            bracket_stack = 0
            while j >= 0:
                if temp[j] == ')':
                    bracket_stack += 1
                elif temp[j] == '(':
                    bracket_stack -= 1
                    if bracket_stack < 0:
                        temp = temp[:j+1] + '(' + temp[j+1:]
                        i += 1
                        break
                else:
                    pass
                j -= 1
            temp = temp[:i] + ')' + temp[i:]
            i += 1

        i += 1

    pro_logic = temp

    # 根据真值表进行计算
    for true_table_id in range(int(math.pow(2, var_num))):
        logic_result = formula_calculate(pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, 0, False)

        if logic_result[0] == 1:
            true_states.append(true_table_id)

    if len(true_states) == 0:
        result = 'always false'
    elif len(true_states) == int(math.pow(2, var_num)):
        result = 'always true'
    else:
        result = 'true states: ' + '\n'
        temp_str = ''
        for true_table_id in true_states:
            for var in var_list:
                temp_str += var + ' : ' + str(true_table[var][true_table_id]) + ' , '
            temp_str = temp_str.strip().strip(',') + '\n'
            result += temp_str
            temp_str = ''

    print(pro_logic)
    return result