import sympy as sp

def oneBaseCase(base, symbol, num, equation, array):
    if num > 6:
        return array
    basestr = str(base)
    subEquation = equation.replace(f'{symbol}(n-1)', f'({basestr})')

    if "n" in subEquation:
        newEquation = subEquation.replace(f'n', f'({num})')
        subEquation = newEquation

    expr = sp.sympify(subEquation)
    result = expr.evalf()
    formattedResult = '{:.15f}'.format(result).rstrip('0').rstrip('.')
    array.append(symbol + "(" + str(num) + ")"+ "=" + formattedResult)
    #print("num: " + str(num) + "\t"+" array:" + array)
    print(f"{symbol}({num}) = {formattedResult}")
    return oneBaseCase(result, symbol, num+1, equation, array)

def twoBaseCase(base1, base2, symbol, num, equation, array):
    if num > 7:
        return array
    base1str = str(base1)
    base2str = str(base2)
    subEquation = equation.replace(f'{symbol}(n-1)', f'({base2str})')
    subEquation = subEquation.replace(f'{symbol}(n-2)', f'({base1str})')

    if "n" in subEquation:
        newEquation = subEquation.replace(f'n', f'({num})')
        subEquation = newEquation

    expr = sp.sympify(subEquation)
    result = expr.evalf()
    formattedResult = '{:.15f}'.format(result).rstrip('0').rstrip('.')
    array.append(symbol + "(" + str(num) + ")" + "=" + formattedResult)
    print(f"{symbol}({num}) = {formattedResult}")
    base1 = base2
    base2 = result
    return twoBaseCase(base1, base2, symbol, num+1, equation, array)

def threeBaseCase(base1, base2, base3, symbol, num, equation, array):
    if num > 8:
        return array
    base1str = str(base1)
    base2str = str(base2)
    base3str = str(base3)
    subEquation = equation.replace(f'{symbol}(n-1)', f'({base3str})')
    subEquation = subEquation.replace(f'{symbol}(n-2)', f'({base2str})')
    subEquation = subEquation.replace(f'{symbol}(n-3)', f'({base1str})')

    if "n" in subEquation:
        newEquation = subEquation.replace(f'n', f'({num})')
        subEquation = newEquation

    expr = sp.sympify(subEquation)
    result = expr.evalf()
    formattedResult = '{:.15f}'.format(result).rstrip('0').rstrip('.')
    array.append(symbol + "(" + str(num) + ")" + "=" + formattedResult)
    print(f"{symbol}({num}) = {formattedResult}")
    base1 = base2
    base2 = base3
    base3 = result
    return threeBaseCase(base1, base2, base3, symbol, num+1, equation, array)
