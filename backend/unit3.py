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
    return oneBaseCase(result, symbol, num+1, equation,array)

def twoBaseCase(base1, base2, symbol, num, equation):
    if num > 7:
        return
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
    print(f"{symbol}({num}) = {formattedResult}")
    base1 = base2
    base2 = result
    twoBaseCase(base1, base2, symbol, num+1, equation)

def threeBaseCase(base1, base2, base3, symbol, num, equation):
    if num > 8:
        return
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
    print(f"{symbol}({num}) = {formattedResult}")
    base1 = base2
    base2 = base3
    base3 = result
    threeBaseCase(base1, base2, base3, symbol, num+1, equation)

def getFirstBaseCase(symbol, initialCondition):
    #initialCondition = input("Enter the initial condition. " + symbol + "(1) = ")
    numEqual = getequal(initialCondition)  # get the position of the equal sign
    iCondition = str(initialCondition[numEqual:len(initialCondition)])  # subset of the entered string after the equal sign which should be the num
    print(iCondition)
    intCondition = int(iCondition)
    return intCondition

def getSecondBaseCase(symbol):
    initialCondition = input("Enter the second base case condition. " + symbol + "(2) = ")
    numEqual = getequal(initialCondition)  # get the position of the equal sign
    iCondition = str(initialCondition[numEqual:len(initialCondition)])  # subset of the entered string after the equal sign which should be the num
    print(iCondition)
    intCondition = int(iCondition)
    return intCondition

def getThirdBaseCase(symbol):
    initialCondition = input("Enter the third base case condition. " + symbol + "(3) = ")
    numEqual = getequal(initialCondition)  # get the position of the equal sign
    iCondition = str(initialCondition[numEqual:len(initialCondition)])  # subset of the entered string after the equal sign which should be the num
    print(iCondition)
    intCondition = int(iCondition)
    return intCondition

def getEquation(symbol, input):
    #relationInput = input("Enter the recurrence relation (ex S(n) = S(n-1) + 10). " + symbol + "(n) = ")
    #relationInputTrim = relationInput.replace(" ", "")  # gets rid of spaces
    relationInputTrim = input.replace(" ", "")
    print(relationInputTrim)
    rightSide = getequal(relationInputTrim)
    equation = relationInputTrim[rightSide:len(relationInputTrim)]
    return equation



#this will return the postion of the "=" sign
def getequal(inputequal):
    position = 0
    for i in inputequal:
        position = position + 1
        if i == "=":
            return position
    return 0

def main():
    try:
        symbol = input("What symbol are you using? S(1) would be using S as a symbol. : ")
        numBaseCases = input("How many base cases do you have? (1,2, or 3): ")
        intBaseCases = int(numBaseCases)
        if intBaseCases == 1:
            base1 = getFirstBaseCase(symbol)
            equation = getEquation(symbol)
            oneBaseCase(base1, symbol, 2, equation)
        elif intBaseCases == 2:
            base1 = getFirstBaseCase(symbol)
            base2 = getSecondBaseCase(symbol)
            equation = getEquation(symbol)
            twoBaseCase(base1, base2, symbol, 3, equation)
        elif intBaseCases == 3:
            base1 = getFirstBaseCase(symbol)
            base2 = getSecondBaseCase(symbol)
            base3 = getThirdBaseCase(symbol)
            equation = getEquation(symbol)
            threeBaseCase(base1, base2, base3, symbol, 4, equation)
        else:
            print("cannot handle " + numBaseCases + " base cases. This can only handle between 1-3 base cases")

    except ValueError:
        print("Invalid input. Please enter valid integers.")


if __name__ == "__main__":
    main()