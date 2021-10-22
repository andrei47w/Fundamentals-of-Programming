def add_function(function_list, function_name, operation, param):
    """
    Adds a new function to the functions list
    :param function_list: the old function list
    :param function_name: string of the nre function's name
    :param operation: string of the actual operation
    :param param: string of all the parameters used
    :return: new function list
    """
    # function_list.append([function_name, operation, param_list])
    new_function = str()
    new_function += 'def '
    new_function += function_name
    new_function += '('
    new_function += param
    new_function += '): return '
    new_function += operation
    # print(new_function)

    new_list = []
    new_list.append(function_name)
    new_list.append(new_function)
    new_list.append(param)

    function_list.append(new_list)

    return function_list


def list_functions(function_list, function_name):
    ok = 0
    for i in range(len(function_list)):
        if function_list[i][0] == function_name:
            print(function_list[i][1])
            ok = 1
            break
    if ok == 0:
        print('ERROR: No such function was found')


def eval_function(function_list, function_name, param):
    ok = 0
    for i in range(len(function_list)):
        if function_list[i][0] == function_name:
            def_param = str()
            def_param += function_list[i][2]
            def_param += ' = '
            def_param += param
            try:
                exec(def_param)
                raise ValueError("ERROR: Wrong parameters")
            except:
                pass
            temp_function = function_list[i][1]
            temp_function = str(temp_function[temp_function.find(': return')+8:])
            print_str = str('print(')
            print_str += temp_function
            print_str += ')'
            exec(print_str)

            ok = 1
    if ok == 0:
        print('ERROR: No such function was found')


def console(function_list):
    print('\n\n     MENU:\n'
          '1. add function_name(p1,p2,...,pn)=p1(+|-)p2(+|-)p3(+|-)...(+|-)pn. This adds the given Mamba function to you program\n'
          '2. list function_name. This displays the correct Python code of the given function to the console\n'
          '3. eval function_name(actual_parameters). This displays on the console the result of calling the function with the given parameters\n'
          '     Input the command: ')
    cmd = input()
    command = str(cmd[:cmd.find(' ')])
    """
    function_name = str(cmd[cmd.find(' ') + 1:cmd.find('(')])
    param = str(cmd[cmd.find('(') + 1:cmd.find(')')])
    param += ','
    param_list = []
    while len(param) != 0:
        param_list.append(param[:param.find(',')])
        param = param[param.find(',') + 1:]
    operation = str(cmd[cmd.find('=') + 1:])
    # print(command, function_name, param_list, operation, sep='\n')
    """
    if command == 'add':
        function_name = str(cmd[cmd.find(' ') + 1:cmd.find('(')])
        param = str(cmd[cmd.find('(') + 1:cmd.find(')')])
        operation = str(cmd[cmd.find('=') + 1:])
        # print(command, function_name, param, operation, sep='\n')
        console(add_function(function_list, function_name, operation, param))
    elif command == 'list':
        function_name = str(cmd[cmd.find(' ') + 1:])
        list_functions(function_list, function_name)
        console(function_list)
    elif command == 'eval':
        function_name = str(cmd[cmd.find(' ') + 1:cmd.find('(')])
        param = str(cmd[cmd.find('(') + 1:cmd.find(')')])
        eval_function(function_list, function_name, param)
        console(function_list)
    else:
        print("ERROR: Unknown command")
        console(function_list)


if __name__ == '__main__':
    function_list = []
    console(function_list)
#  add alternate_sum(first,second,third,fourth)=first-second+third-fourth
