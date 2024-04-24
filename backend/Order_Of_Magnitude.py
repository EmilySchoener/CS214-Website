import math
def get_function(function_str):
    try:
        if 'log' in function_str:
            function_str = function_str.replace('log', 'math.log')
        if 'x' in function_str and not function_str.startswith(('x', '-', '+', '*', '/', '**')):
            function_str = function_str.replace('x', '*x')
        return lambda x: eval(function_str)
    except:
        print("Invalid function expression.")
        return get_function(function_str)


# Define a function to find C1 and C2
def find_constants(f, g, x0):

    if x0 <= 0:
        return []
    if f == None or g == None:
        return []
    if 'log' in f:
        func_f = math.log
    else:
        func_f = get_function(f)

    if 'log' in g:
        func_g = math.log
    else:
        func_g = get_function(g)

    fx0 = func_f(x0)
    gx0 = func_g(x0)

    ord_f = abs(fx0)
    ord_g = abs(gx0)


    C1 = 1 / abs(gx0)
    C2 = abs(fx0) - C1 * abs(gx0)
    nO = max(ord_f, ord_g)
    consts = [C1, C2, nO]
    return consts

