# -*- coding: utf-8 -*-
import math
import traceback

def arg_check(pro_logic, i):
    temp = ''
    while i < len(pro_logic):
        if pro_logic[i].isalpha() or pro_logic[i].isdigit():
            temp += pro_logic[i]
            i += 1
        else:
            break
    return [i - 1, temp]



def syntax_check(pro_logic, custom_logic_list):
    num_logic_word = ['0', '1']
    basic_logic_word = ['~', '&', '|', '^']
    derivation_word = ['->', '<->']
    # 语法检测结果 错误说明 变元列表
    result = [True, 'no error', []]


    # 无自定义的逻辑联结词
    if len(custom_logic_list) == 0:
        i = 0
        # 检测推导符两边情况
        temp_num = pro_logic.count('->')
        temp_str = pro_logic.split('->', temp_num)
        for s in temp_str:
            if s.strip() == '':
                result = [False, "-> left or right cnt't be null", []]
                return result
        temp_num = pro_logic.count('<->')
        temp_str = pro_logic.split('<->', temp_num)
        for s in temp_str:
            if s.strip() == '':
                result = [False, " <-> left or right cnt't be null", []]
                return result

        # 状态
        state = 0
        '''
        0 : begin    -> <->
        1 : 0 1
        2 : 命题变元 )
        3 : ~
        4 : & | ^
        '''
        # 括号栈
        bracket_stack = []
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
                        if arg_result[1] not in result[2]:
                            result[2].append(arg_result[1])

                        state = 2

                    elif pro_logic[i] == '~':
                        state = 3
                    elif pro_logic[i] == '(':
                        # 记录当且状态
                        bracket_stack.append(state)
                        state = 0
                    else:
                        result = [False, 'error in ' + pro_logic[i - 1:i + 1], []]
                        break
                    i += 1


                elif state == 1 or state == 2:
                    if  pro_logic[i] == ' ':
                        pass
                    elif pro_logic[i] == '&' or pro_logic[i] == '|' or pro_logic[i] == '^':
                        state = 4
                    elif (pro_logic[i] == '-' and pro_logic[i+1] == '>'):
                        i += 1
                        state = 0
                    elif (pro_logic[i] == '<' and pro_logic[i+1] == '-' and pro_logic[i+2] == '>'):
                        i += 2
                        state = 0
                    elif pro_logic[i] == ')':
                        bracket_stack.pop()
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

    # 有自定义的逻辑联结词
    else:

        # # 检测说明是否正确
        # for i in range(len(inputs)):
        #     if i == 0:
        #         pro_logic = inputs[i]
        #     else:
        #         temp = inputs[i][1:].split(' ')
        #
        #         mark = False
        #         for e in temp[0]:
        #             if ~e.isalpha() and ~e.isdigit():
        #                 mark = True
        #                 break
        #         if mark:
        #             result = [False, 'error in ' + inputs[i]]
        #             break
        #         custom_logic_word.append(temp[0])
        #
        #         if not temp[1].isdigit():
        #             result = [False, 'error in ' + inputs[i]]
        #             break
        #         custom_logic_element_num.append(temp[1])
        #
        #         mark = False
        #         if len(temp[2]) == math.pow(2, int(temp[1])):
        #             for e in temp[2]:
        #                 if e != '0' and e != '1':
        #                     mark = True
        #                     break
        #         else:
        #             mark = True
        #         if mark:
        #             result = [False, 'error in ' + inputs[i]]
        #             break
        #
        #         custom_logic_truth_table.append(temp[2])

        # 说明不正确
        # if result[0] == False:
        #     return result

        # 状态
        state = 0
        '''
        0 : begin    -> <->
        1 : 0 1
        2 : 命题变元 )
        3 : ~
        4 : & | ^
        5 : custome
        6 : custome 命题变元
        7 : custome ~
        8 : custome & | ^
        9 : custome ,
        '''
        # 括号栈
        bracket_stack = []
        custom_stack = 0

        pass




    return result


# 基本逻辑联结词的计算
def basic_logic_calculate(arg1, arg2, op):
    result = 0
    if op == '&':
        result = int(arg1) and int(arg2)
    elif op == '|':
        result = int(arg1) or int(arg2)
    elif op == '^':
        result = int(arg1) ^ int(arg2)
    elif op == '->':
        if int(arg1) == 1 and int(arg2) == 0:
            result = 0
        else:
            result = 1
    elif op == '<->':
        if arg1 == arg2:
            result = 1
        else:
            result = 0
    return result



# 自定义逻辑联结词的计算
def custom_logic_calculate(custom_logic_word, pro_logic, true_table, true_table_id, begin_index):
    result = 0
    return result


# 对左右两侧的命题进行计算
# 出现~和(时进行递归运算
def formula_calculate(pro_logic, true_table, true_table_id, begin_index, not_mark):
    end_index = len(pro_logic) - 1
    result = [1, end_index]     #end_index 已分析的下标
    arg_1 = -1
    arg_2 = -1
    if not_mark:
        op = '~'
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
                        result[0] = -1
                        return result
                # 正确处理后要返回
                elif op == '~':
                    if arg_1 == -1:
                        arg_1 = 1 ^ int(pro_logic[i])
                        result[0] = arg_1
                        result[1] = i
                        return result
                    else:
                        result[0] = -1
                        return result
                else:
                    if arg_1 == -1:
                        result[0] = -1
                        return result
                    else:
                        arg_1 = basic_logic_calculate(arg_1, pro_logic[i], op)
                        op = ''


            elif pro_logic[i].isalpha():
                arg_result = arg_check(pro_logic, i)
                i = arg_result[0]
                arg_name = arg_result[1]
                arg_value = true_table[arg_name][true_table_id]

                if op == '':
                    if arg_1 == -1:
                        arg_1 = int(arg_value)

                    else:
                        result[0] = -1
                        return result
                elif op == '~':
                    if arg_1 == -1:
                        arg_1 = 1 ^ int(arg_value)
                        result[0] = arg_1
                        result[1] = i
                        return result
                    else:
                        result[0] = -1
                        return result
                else:
                    if arg_1 == -1:
                        result[0] = -1
                        return result
                    else:
                        arg_1 = basic_logic_calculate(arg_1, arg_value, op)
                        op = ''


            elif pro_logic[i] == '&' or pro_logic[i] == '|' or pro_logic[i] == '^':
                if op == '' :
                    op = pro_logic[i]
                else:
                    result[0] = -1
                    return result
            elif pro_logic[i] == '-' and pro_logic[i+1] == '>' :
                if op == '' :
                    op = '->'
                else:
                    result[0] = -1
                    return result
                i += 1

            elif pro_logic[i] == '<' and pro_logic[i+1] == '-' and pro_logic[i+2] == '>' :
                if op == '' :
                    op = '<->'
                else:
                    result[0] = -1
                    return result
                i += 2

            elif pro_logic[i] == '~':
                temp_result = formula_calculate(pro_logic, true_table, true_table_id, i+1, True)
                arg_value = int(temp_result[0])
                i = temp_result[1]

                if op == '':
                    if arg_1 == -1:
                        arg_1 = int(arg_value)
                    else:
                        result[0] = -1
                        return result
                elif op == '~':
                    if arg_1 == -1:
                        arg_1 = 1 ^ int(arg_value)
                        result[0] = arg_1
                        result[1] = i
                        return result
                    else:
                        result[0] = -1
                        return result
                else:
                    if arg_1 == -1:
                        result[0] = -1
                        return result
                    else:
                        arg_1 = basic_logic_calculate(arg_1, arg_value, op)
                        op = ''
            elif pro_logic[i] == '(':
                temp_result = formula_calculate(pro_logic, true_table, true_table_id, i+1, False)
                arg_value = temp_result[0]
                i = temp_result[1]

                if op == '':
                    if arg_1 == -1:
                        arg_1 = int(arg_value)
                    else:
                        result[0] = -1
                        return result
                elif op == '~':
                    if arg_1 == -1:
                        arg_1 = 1 ^ int(arg_value)
                        result[0] = arg_1
                        result[1] = i
                        return result
                    else:
                        result[0] = -1
                        return result
                else:
                    if arg_1 == -1:
                        result[0] = -1
                        return result
                    else:
                        arg_1 = basic_logic_calculate(arg_1, arg_value, op)
                        op = ''

            elif pro_logic[i] == ')':
                if arg_1 == -1:
                    result[0] = -1
                    return result
                else:
                    result[0] = arg_1
                    result[1] = i
                    return result
            else:
                result[0] = -1
                return result

            i += 1

    except Exception as e:
        traceback.print_exc()

    result[0] = arg_1
    return result



def pro_logic_check(pro_logic, custom_logic_list, var_list):
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

    # 提取命题公式
    temp = '('
    for i in range(len(pro_logic)):
        if (pro_logic[i] == '<' and pro_logic[i + 1] == '-' and pro_logic[i + 2] == '>') \
                or (pro_logic[i] == '-' and pro_logic[i + 1] == '>' and pro_logic[i - 1] != '<'):
            temp += ')' + pro_logic[i]
        elif pro_logic[i] == '>' and pro_logic[i - 1] == '-':
            temp += pro_logic[i] + '('
        else:
            temp += pro_logic[i]
    temp += ')'
    pro_logic = temp

    # 根据真值表进行计算
    for true_table_id in range(int(math.pow(2, var_num))):
        logic_result = formula_calculate(pro_logic, true_table, true_table_id, 0, False)

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

    return result