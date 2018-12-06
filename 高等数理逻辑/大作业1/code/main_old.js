
function error_print(pro_logic, begin_index, end_index, err_mes) {
    if(err_mes === ''){
        var str_1 = pro_logic.substring(0, begin_index);
        var str_2 = pro_logic.substring(begin_index, end_index + 1);
        var str_3 = pro_logic.substring(end_index + 1);

        var op = document.getElementById("output");
        op.style.display="inline";

        var oFont1=document.createElement("FONT");
        var oText1=document.createTextNode(str_1);
        oFont1.style.color="black";
        oFont1.appendChild(oText1);
        op.appendChild(oFont1);

        var oFont2=document.createElement("FONT");
        var oText2=document.createTextNode(str_2);
        oFont2.style.color="red";
        oFont2.appendChild(oText2);
        op.appendChild(oFont2);

        var oFont3=document.createElement("FONT");
        var oText3=document.createTextNode(str_3);
        oFont3.style.color="black";
        oFont3.appendChild(oText3);
        op.appendChild(oFont3);
    }
    else {
        document.getElementById("output").style.display="inline";
        document.getElementById("output").value = err_mes;
    }
}


function isalpha(s) {
    return ((s >= 'a' && s <= 'z') || (s >= 'A' && s <= 'Z'));
}
function isdigit(s) {
    return ((s >= '0' && s <= '9'));
}

/**
 * @return {boolean}
 */
function T_0_check(last_true_table) {
    return (parseInt(last_true_table[0]) === 0);
}

/**
 * @return {boolean}
 */
function T_1_check(last_true_table){
    return (parseInt(last_true_table[last_true_table.length-1]) === 1);
}

// 计算真值表某行元素中1的个数
function cal_one_num(n){
    var res = 0;

    while(n !== 0){
        n = n - Math.pow(2, parseInt(Math.log2(n)));
        res += 1;
    }
    return res;
}

/**
 * @return {boolean}
 */
function L_check(last_true_table){
    var result = true;
    var mark_1 = 0;  // 1 : even  0 : odd
    var mark_2 = 0;  // 1 : odd  0 : even

    for (var i = 0; i < last_true_table.length; i++){
        var table_num = parseInt(last_true_table[i]);
        var one_num = cal_one_num(i);
        if (table_num === 1){
            if (one_num % 2 === 0){
                mark_1 += 1;
            }
            else{
                mark_2 += 1;
            }
        }
        else{
            if (one_num % 2 === 0){
                mark_2 += 1;
            }
            else{
                mark_1 += 1;
            }
        }

    }

    if (mark_1 !== last_true_table.length && mark_2 !== last_true_table.length){
        result = false;
    }

    return result;
}


/**
 * @return {boolean}
 */
function M_check(ele_num, last_true_table){
    var result = true;

    for (var i = 0; i < last_true_table.length; i++){
        var table_num = parseInt(last_true_table[i]);
        if (table_num === 1){
            var ele_str = i.toString(2);
            while (ele_str.length < ele_num){
                ele_str = '0' + ele_str;
            }

            var j = 0;
            while (j < ele_str.length){
                if (ele_str[j] === '1'){
                    j += 1;
                }
                else{
                    var temp_ele_str = ele_str.substring(0,j) + '1' + ele_str.substring(j+1);
                    var temp_table_num = parseInt(last_true_table[parseInt(temp_ele_str, 2)]);
                    // 1 指向 0
                    if (temp_table_num === 0){
                        result = false ;
                        return result;
                    }
                    j += 1;
                }
            }
        }
    }


    return result;
}


/**
 * @return {boolean}
 */
function S_check(last_true_table){
    var result = true;

    var l = last_true_table.length;
    for (var i = 0; i < parseInt(l/2); i++){
        if (parseInt(last_true_table[i]) === parseInt(last_true_table[l-1-i])){
            result = false;
            break;
        }
    }

    return result;
}

// 自定义逻辑联结词    {'f' : [2, 1101], }
function com_set_calculate(custom_logic_list){
    var result = false;

    var T_0_mark = false;
    var T_1_mark = false;
    var L_mark = false;
    var M_mark = false;
    var S_mark = false;

    for (var logic_name in custom_logic_list){
        var ele_num = parseInt(custom_logic_list[logic_name][0]);
        var last_true_table = custom_logic_list[logic_name][1];
        if (!T_0_mark){
            T_0_mark = !T_0_check(last_true_table);
        }
        if (!T_1_mark){
            T_1_mark = !T_1_check(last_true_table);
        }
        if (!L_mark){
            L_mark = !L_check(last_true_table);
        }
        if (!M_mark){
            M_mark = !M_check(ele_num, last_true_table);
        }
        if (!S_mark){
            S_mark = !S_check(last_true_table);
        }

        if (T_0_mark && T_1_mark && L_mark && M_mark && S_mark){
            result = true;
            break;
        }
    }
    window.alert(T_0_mark.toString() + ' ' + T_1_mark.toString() + ' ' + L_mark.toString() + ' ' + M_mark.toString() + ' ' + S_mark.toString());

    return result;
}




function arg_check(pro_logic, i) {
    var temp = '';
    while (i < pro_logic.length){
        if (isalpha(pro_logic[i]) || isdigit(pro_logic[i])){
            temp += pro_logic[i];
            i += 1;
        }
        else{
            break;
        }
    }
    return [i - 1, temp]
}

// 命题公式语法检查
function pro_logic_syntax_check(pro_logic, custom_logic_list, zero_ele_custom_logic_list) {
    // 语法检测结果 错误说明 变元列表
    var result = [true, 'no error', []];

    // 检测推导符两边情况
    var i;
    var temp = '';
    for (i = 0; i < pro_logic.length; i++){
        if (pro_logic[i] === '→' || pro_logic[i] === '↔'){
            if (temp === ''){
                result = [false, "→/↔ left or right cnt't be null", []];
                return result;
            }
            else {
                temp = '';
            }
        }
        else {
            if (pro_logic[i] !== ' '){
                temp += pro_logic[i];
            }
        }
    }


    // 状态
    var state = 0;
    /*
    0 : begin  (  → ↔
    1 : 0 1
    2 : 命题变元 )  custome_end
    3 : ¬
    4 : ∧ ∨ ⊕
    5 : custome_begin

    */
    // 括号栈
    var bracket_stack = [];
    // 判断是否还在custom内,括号全匹配上
    var custom_stack = 0;

    try {
        i = 0;
        while (i < pro_logic.length){
            if (state === 0 || state === 3 || state === 4){
                if (pro_logic[i] === ' '){
                    i += 1;
                    continue;
                }
                else if(pro_logic[i] === '0' || pro_logic[i] === '1'){
                    state = 1;
                }

                else if(isalpha(pro_logic[i])){
                    var arg_result = arg_check(pro_logic, i);
                    // 更新下标
                    i = arg_result[0];
                    // 添加变元
                    var arg_name = arg_result[1];
                    // 普通命题变元
                    if (!(arg_name in custom_logic_list)){
                        if((result[2].indexOf(arg_name) === -1) && (!(arg_name in zero_ele_custom_logic_list))){
                            result[2].push(arg_name);
                        }
                        state = 2;
                    }
                    // 自定义逻辑联结词
                    else{
                        state = 5;
                    }
                }
                else if (pro_logic[i] === '¬'){
                    state = 3;
                }
                else if (pro_logic[i] === '('){
                    // 记录当且状态
                    bracket_stack.push(state);
                    state = 0;
                    if (custom_stack > 0){
                        custom_stack += 1;
                    }
                }
                else{
                    result = [false, 'error in ' + pro_logic[i], []];
                    break;
                }

                i += 1;
            }

            else if (state === 1 || state === 2){
                if (pro_logic[i] === ' '){
                    i += 1;
                    continue;
                }
                else if (pro_logic[i] === '∧' || pro_logic[i] === '∨' || pro_logic[i] === '⊕'){
                    state = 4;
                }
                else if (pro_logic[i] === '→' || pro_logic[i] === '↔'){
                    state = 0;
                }
                else if (pro_logic[i] === ')'){
                    bracket_stack.pop();
                    if (custom_stack > 0){
                        custom_stack -= 1;
                    }
                }
                else if (pro_logic[i] === ',' && custom_stack > 0){
                    state = 0;
                }
                else{
                    result = [false, 'error in ' + pro_logic[i], []];
                    break;
                }
                i += 1;
            }

            else if (state === 5){
                if (pro_logic[i] === '('){
                    bracket_stack.push(state);
                    custom_stack += 1;
                    state = 0;
                }
                else{
                    result = [false, 'error in ' + pro_logic[i], []];
                    break;
                }
                i += 1;
            }
            else{
                result = [false, 'error in ' + pro_logic[i], []];
                break;
            }

        }

    }
    catch (err){
        window.alert(err.message);
        result = [false, 'error in ' + pro_logic[i], []];
    }


    if (result[0] === true ){
        if (bracket_stack.length !== 0){
            result = [false, 'lost )', []]
        }

        if (!(state === 0 || state === 1 || state === 2 )){
            result = [false, 'proposition not complete', []];
        }
    }

    return result;
}


// 基本逻辑联结词的计算
function basic_logic_calculate(arg1, arg2, op){
    var result = 0;
    arg1 = parseInt(arg1);
    arg2 = parseInt(arg2);
    if (op === '∧'){
        result = arg1 && arg2;
    }
    else if (op === '∨'){
        result = arg1 || arg2;
    }
    else if (op === '⊕'){
        result = arg1 ^ arg2;
    }
    else if (op === '→'){
        if (arg1 === 1 && arg2 === 0){
            result = 0;
        }
        else{
            result = 1;
        }
    }
    else if (op === '↔'){
        if (arg1 === arg2){
            result = 1;
        }
        else{
            result = 0;
        }
    }
    return result
}


// 自定义逻辑联结词的计算
function custom_logic_calculate(custom_logic_word, pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, begin_index){
    var end_index = pro_logic.length - 1;
    var result = [0, end_index];

    var arg_value_list = [];

    // 括号栈
    var bracket_stack = 0;
    var i = begin_index;
    if (pro_logic[i] === '('){
        bracket_stack += 1;
        i += 1;
    }
    else{
        window.alert('lost ( after ' + custom_logic_word);
        throw SyntaxError();
    }

    var element_num = 0;
    var element = '';
    while(i < pro_logic.length){
        if (pro_logic[i] === ' '){
            i += 1;
            continue;
        }
        else if (pro_logic[i] === '('){
            bracket_stack += 1;
            element += pro_logic[i];
        }
        else if (pro_logic[i] === ')'){
            bracket_stack -= 1;
            element += pro_logic[i];
        }
        // 收集到自定义逻辑联结词的一个完整命题变元
        else if (pro_logic[i] === ',' && bracket_stack === 1){
            var temp_result = formula_calculate(element, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, 0, false);
            if (temp_result[0] === 0 || temp_result[0] === 1){
                arg_value_list.push(temp_result[0]);
            }
            else{
                arg_value_list.push(0);
            }
            element = '';
            element_num += 1;
        }

        else{
            element += pro_logic[i];
        }

        // 整个自定义的逻辑联结词结束
        if (bracket_stack <= 0){
            if (element[element.length-1] === ')'){
                element = element.substring(0,element.length-1);
            }

            temp_result = formula_calculate(element, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, 0, false);
            if (temp_result[0] === 0 || temp_result[0] === 1){
                arg_value_list.push(temp_result[0]);
            }
            else{
                arg_value_list.push(0);
            }
            element = '';
            element_num += 1;

            result[1] = i;
            break;
        }

        i += 1;
    }

    if (element_num !== parseInt(custom_logic_list[custom_logic_word][0])){
        window.alert(custom_logic_word + ' element num is not right');
        throw SyntaxError();
    }

    var arg_value_str = '';
    for (i = 0; i < arg_value_list.length; i++){
        arg_value_str += String(arg_value_list[i]);
    }
    

    result[0] = parseInt(custom_logic_list[custom_logic_word][1][parseInt(arg_value_str,2)]);
    return result;
}


// 对左右两侧的命题进行计算
// 出现¬和(时进行递归运算
function formula_calculate(pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, begin_index, not_mark){
    var end_index = pro_logic.length - 1;
    var result = [0, end_index];     // end_index 已分析的下标
    var arg_1 = -1;
    var op = '';
    if (not_mark){
        op = '¬';
    }
    else{
        op = '';
    }

    var i = begin_index;
    try{
        while(i < pro_logic.length){
            if (pro_logic[i] === ' '){
                i += 1;
                continue;
            }
            else if (pro_logic[i] === '0' || pro_logic[i] === '1'){
                if (op === ''){
                    if (arg_1 === -1){
                        arg_1 = parseInt(pro_logic[i]);
                    }
                    else{
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }
                }
                // 正确处理后要返回
                else if (op === '¬'){
                    if (arg_1 === -1){
                        arg_1 = 1 ^ parseInt(pro_logic[i]);
                        result[0] = arg_1;
                        result[1] = i;
                        return result;
                    }
                    else{
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }
                }
                else{
                    if (arg_1 === -1){
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }
                    else{
                        arg_1 = basic_logic_calculate(arg_1, pro_logic[i], op);
                        op = '';
                    }
                }
            }

            else if (isalpha(pro_logic[i])){
                var arg_result = arg_check(pro_logic, i);
                i = arg_result[0];
                var arg_name = arg_result[1];
                var arg_value = 0;

                // 自定义逻辑联结词
                if (arg_name in custom_logic_list){
                    var temp_result = custom_logic_calculate(arg_name, pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, i + 1);
                    arg_value = temp_result[0];
                    i = temp_result[1];
                }
                else if (arg_name in zero_ele_custom_logic_list){
                    arg_value = zero_ele_custom_logic_list[arg_name];
                }
                else{
                    arg_value = true_table[arg_name][true_table_id];
                }


                if (op === ''){
                    if (arg_1 === -1){
                        arg_1 = parseInt(arg_value);
                    }
                    else{
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }

                }
                else if (op === '¬'){
                    if (arg_1 === -1){
                        arg_1 = 1 ^ parseInt(arg_value);
                        result[0] = arg_1;
                        result[1] = i;
                        return result;
                    }
                    else{
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }
                }
                else{
                    if (arg_1 === -1){
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }
                    else{
                        arg_1 = basic_logic_calculate(arg_1, arg_value, op);
                        op = '';
                    }
                }

            }

            else if (pro_logic[i] === '∧' || pro_logic[i] === '∨' || pro_logic[i] === '⊕'){
                if (op === ''){
                    op = pro_logic[i];
                }
                else{
                    result[0] = -1;
                    return result;
                }
            }
            else if (pro_logic[i] === '→' || pro_logic[i] === '↔'){
                if (op === ''){
                    op = pro_logic[i];
                }
                else{
                    window.alert('error in ' + pro_logic[i]);
                    throw SyntaxError();
                }
            }
            else if (pro_logic[i] === '¬'){
                temp_result = formula_calculate(pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, i+1, true);
                arg_value = parseInt(temp_result[0]);
                i = temp_result[1];

                if (op === ''){
                    if (arg_1 === -1){
                        arg_1 = parseInt(arg_value);
                    }
                    else{
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }
                }
                else if (op === '¬'){
                    if (arg_1 === -1){
                        arg_1 = 1 ^ parseInt(arg_value);
                        result[0] = arg_1;
                        result[1] = i;
                        return result;
                    }
                    else{
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }
                }
                else{
                    if (arg_1 === -1){
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }
                    else{
                        arg_1 = basic_logic_calculate(arg_1, arg_value, op);
                        op = '';
                    }
                }
            }
            else if (pro_logic[i] === '('){
                temp_result = formula_calculate(pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, i+1, false);
                arg_value = temp_result[0];
                i = temp_result[1];

                if (op === ''){
                    if (arg_1 === -1){
                        arg_1 = parseInt(arg_value);
                    }
                    else{
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }
                }
                else if (op === '¬'){
                    if (arg_1 === -1){
                        arg_1 = 1 ^ parseInt(arg_value);
                        result[0] = arg_1;
                        result[1] = i;
                        return result;
                    }
                    else{
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }
                }
                else{
                    if (arg_1 === -1){
                        window.alert('error in ' + pro_logic[i]);
                        throw SyntaxError();
                    }
                    else{
                        arg_1 = basic_logic_calculate(arg_1, arg_value, op);
                        op = '';
                    }
                }
            }
            else if (pro_logic[i] === ')'){
                if (arg_1 === -1){
                    window.alert('error in ' + pro_logic[i]);
                    throw SyntaxError();
                }
                else{
                    result[0] = arg_1;
                    result[1] = i;
                    return result;
                }
            }
            else{
                window.alert('error in ' + pro_logic[i]);
                throw SyntaxError();
            }
            i += 1;
        }
    }
    catch (err){
        window.alert(err.message);
        result = [0, end_index];
    }

    result[0] = arg_1;
    return result
}


function cut_formula(formula) {
    var basic_logic_list = ['∧', '∨', '⊕', '→', '↔'];
    var i,j,k;
    for (k = 0; k < basic_logic_list.length; k++){
        var basic_logic_word = basic_logic_list[k];
        i = 0;
        while (i < formula.length){
            if (formula[i] === basic_logic_word){
                // 填充右边的括号
                j = i + 1;
                var bracket_stack = 0;
                while (j < formula.length){
                    if (formula[j] === '('){
                        bracket_stack += 1;
                    }
                    else if(formula[j] === ')'){
                        bracket_stack -= 1;
                        if (bracket_stack < 0){
                            formula = formula.substring(0,j) + ')' + formula.substring(j);
                            break;
                        }
                    }
                    // 遇到优先级更高的联结词
                    else if (bracket_stack ===0 && basic_logic_list.includes(formula[j]) && (basic_logic_list.indexOf(formula[j]) > k)){
                        formula = formula.substring(0,j) + ')' + formula.substring(j);
                        break;
                    }
                    j += 1;
                }

                // 填充左边的括号
                j = i - 1;
                bracket_stack = 0;
                while (j >= 0){
                    if (formula[j] === ')'){
                        bracket_stack += 1;
                    }
                    else if (formula[j] === '('){
                        bracket_stack -= 1;
                        if (bracket_stack < 0){
                            formula = formula.substring(0,j+1) + '(' + formula.substring(j+1);
                            i += 1;
                            break;
                        }
                    }
                    else if (bracket_stack ===0 && basic_logic_list.includes(formula[j]) && (basic_logic_list.indexOf(formula[j]) > k)){
                            formula = formula.substring(0,j+1) + '(' + formula.substring(j+1);
                            i += 1;
                            break;
                    }
                    j -= 1;
                }
            }

            i += 1;
        }
    }


    return formula;
}


function pro_logic_calculate(pro_logic, custom_logic_list, zero_ele_custom_logic_list, var_list) {
    var result = 'always true / always false / true status : ';

    // 命题逻辑成立时的真值表列数
    var true_states = [];

    var true_table = {};
    var i;
    for (i = 0; i < var_list.length; i++){
        true_table[var_list[i]] = []
    }

    // 生成真值表
    var var_num = var_list.length;
    for (i = 0; i < Math.pow(2, var_num); i++){
        var true_table_str = i.toString(2);
        while (true_table_str.length < var_num){
            true_table_str = '0' + true_table_str;
        }
        for (var j = 0; j < var_num; j++){
            true_table[var_list[j]].push(parseInt(true_table_str[j]));
        }

    }

    // 以→和↔切分命题公式
    var temp = '(' + pro_logic + ')';
    pro_logic = cut_formula(temp);
    window.alert(pro_logic);

    // 根据真值表进行计算
    var true_table_id;
    for (true_table_id = 0; true_table_id < parseInt(Math.pow(2, var_num)); true_table_id++){
        var logic_result = formula_calculate(pro_logic, custom_logic_list, zero_ele_custom_logic_list, true_table, true_table_id, 0, false);
        if (logic_result[0] === 1){
            true_states.push(true_table_id);
        }
    }

    if (true_states.length === 0){
        result = 'always false';
    }
    else if (true_states.length === parseInt(Math.pow(2, var_num))){
        result = 'always true';
    }
    else{
        result = 'true states: ' + '\n';
        var temp_str = '';
        for (i = 0; i < true_states.length; i++){
            true_table_id = true_states[i];
            for (j = 0; j < var_list.length; j++){
                var var_name = var_list[j];
                temp_str += var_name + ' : ' + String(true_table[var_name][true_table_id]) + ' , ';
            }

            temp_str = temp_str.trim() + '\n';
            result += temp_str;
            temp_str = '';
        }
    }

    return result;
}







function pro_logic() {
    var input_lines = document.getElementById('input').value;
    input_lines = input_lines.trim();

    if(input_lines === ''){
        window.alert('不能输入空内容！');
        return;
    }

    // 命题公式
    var pro_logic_str = '';
    // 自定义逻辑联结词    {'f' : [2, 1101], }
    var custom_logic_list = {};
    var zero_ele_custom_logic_list = {};    // {'h' : 1/0}

    // 切分行
    var line_list = [];
    var temp_str = '';
    var i;
    for (i = 0; i < input_lines.length; i++){
        if (input_lines[i] === '\n' || i === (input_lines.length - 1)){
            temp_str += input_lines[i];
            line_list.push(temp_str.trim());
            temp_str = '';
        }
        else {
            temp_str += input_lines[i];
        }
    }

    // 解析输入
    var line_str = '';
    var custom_logic_name = '', element_num = '', custom_true_table = '';
    for (i = 0; i < line_list.length; i++){
        line_str = line_list[i].trim();
        custom_logic_name = '';
        element_num = '';
        custom_true_table = '';

        if (line_str === ''){
            continue;
        }
        else if(line_str.indexOf('%') !== -1){
            line_str = line_str.split('%')[0].trim();
            if (line_str === ''){
                continue;
            }
        }
        // 自定义逻辑联结词
        if (line_str[0] === '#'){
            line_str = line_str.substring(1).trim();

            var temp = line_str.split(' ');
            custom_logic_name = temp[0];
            element_num = temp[1];
            for (var j = 2; j < temp.length; j++){
                custom_true_table += temp[j];
            }

            if (custom_logic_name in custom_logic_list){
                window.alert('exist custom logic!');
                return;
            }
            else if (Math.pow(2, parseInt(element_num)) !== custom_true_table.length){
                window.alert(custom_logic_name + ' define wrong');
                return;
            }
            else if (parseInt(element_num) === 0){
                zero_ele_custom_logic_list[custom_logic_name] = parseInt(custom_true_table);
            }
            else {
                custom_logic_list[custom_logic_name] = [element_num, custom_true_table]
            }
            
        }
        // 命题公式
        else {
            pro_logic_str = line_str;
        }

    }


    var syntax_result = pro_logic_syntax_check(pro_logic_str, custom_logic_list, zero_ele_custom_logic_list);
    if (syntax_result[0]){
        var pro_logic_result = pro_logic_calculate(pro_logic_str, custom_logic_list, zero_ele_custom_logic_list, syntax_result[2]);
        document.getElementById("output").style.display="inline";
        document.getElementById("output").value = pro_logic_result;
    }
    else {
        window.alert(syntax_result[1]);
    }

}






function com_set() {
    var input_lines = document.getElementById('input').value;
    input_lines = input_lines.trim();

    if(input_lines === ''){
        window.alert('不能输入空内容！');
        return;
    }

    // 自定义逻辑联结词    {'f' : [2, 1101], }
    var custom_logic_list = {};

    // 切分行
    var line_list = [];
    var temp_str = '';
    var i;
    for (i = 0; i < input_lines.length; i++){
        if (input_lines[i] === '\n' || i === (input_lines.length - 1)){
            temp_str += input_lines[i];
            line_list.push(temp_str.trim());
            temp_str = '';
        }
        else {
            temp_str += input_lines[i];
        }
    }

    // 解析输入
    var line_str = '';
    var custom_logic_name = '', element_num = '', true_table = '';
    for (i = 0; i < line_list.length; i++){
        line_str = line_list[i].trim();
        custom_logic_name = '';
        element_num = '';
        true_table = '';

        if (line_str === ''){
            continue;
        }
        else if(line_str.indexOf('%') !== -1){
            line_str = line_str.split('%')[0].trim();
            if (line_str === ''){
                continue;
            }
        }
        // 自定义逻辑联结词
        if (line_str[0] === '#'){
            line_str = line_str.substring(1).trim();

            var temp = line_str.split(' ');
            custom_logic_name = temp[0];
            element_num = temp[1];
            for (var j = 2; j < temp.length; j++){
                true_table += temp[j];
            }

            if (custom_logic_name in custom_logic_list){
                window.alert('exist custom logic!');
                return;
            }
            else if (Math.pow(2, parseInt(element_num)) !== true_table.length){
                window.alert(custom_logic_name + ' define wrong');
                return;
            }
            else if (parseInt(element_num) === 0){
                custom_logic_list[custom_logic_name] = [1, true_table + true_table];
            }
            else {
                custom_logic_list[custom_logic_name] = [element_num, true_table];
            }

        }
        // 命题公式
        else {
            window.alert(line_str);
        }

    }


    var com_set_result = com_set_calculate(custom_logic_list);
    document.getElementById("output").style.display="inline";
    document.getElementById("output").value = com_set_result;

}