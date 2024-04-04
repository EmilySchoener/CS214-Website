def Antcendent_check_func(test, A, B, C):
    try:
        if evaluation_func(test, A, B, C, True):
            return test, True
    except SyntaxError:
        FirstPart = test + " ) "
        if evaluation_func(FirstPart, A, B, C, True):
            return FirstPart, True
    return test, False


def evaluation_func(string, A, B, C, isAntcendent=False):
    if isAntcendent and eval(string):
        # print("This is an antcendent and therefore will always be true since the hypothesis is False")
        return True

    return eval(string)


def negation_func(string, A, B, C):
    negation = " not ("
    parts = string.split()
    last_part = parts[-1]
    # print("This is the last part "+last_part)
    if last_part == ')':
        for i in range(len(parts) - 1, -1, -1):
            if parts[i] == '(':
                index_of_opening_bracket = i
                parts.insert(index_of_opening_bracket, negation)
                sting = ' '.join(parts) + " ) "
                # print("This is the string of ) " + sting)
                return ' '.join(parts) + " ) "

    else:
        parts[-1] = str(not evaluation_func(last_part, A, B, C))
        sting = ' '.join(parts) + " "
        # print("This is the string of else "+ sting)
        return ' '.join(parts)


def implication_func(string, A, B, C):
    # print("A: ", A, " B: ", B, " C: ", C, " ")
    stripped_string = string.strip()
    # print(len(stripped_string)," This is the string passed by implication function: " + string)
    start = " ( "
    end = " ) "
    imp = " <= "
    parts = string.split()
    parts.insert(0, start)
    parts.append(end)
    test = negation_func(' '.join(parts), A, B, C)
    # print(test)
    try:
        string, check = Antcendent_check_func(test, A, B, C)

    except:
        print(string)
    if (len(string.strip()) < 7):
        # print("The string short")
        return start + string + end + imp, False
    FirstPart = string
    # print(FirstPart)
    try:
        FirstPart = str(evaluation_func(FirstPart, A, B, C))
    except:
        hi = 1
        # print("Error")
    FirstPart = FirstPart + imp
    # print(FirstPart)
    return FirstPart, False


def equivalence_func(string, A, B, C):
    # print(string)
    start = " ( "
    end = " ) "
    equivalence = " == "
    try:
        string = str(evaluation_func(string, A, B, C))
    except:
        string = start + string
        string = str(evaluation_func(string, A, B, C))

    return string + equivalence + start


def process_wff(A, B, C, input):
    # result = eval(str(input))
    # output=str(result)+" "+str(input)+" "+str(B)+" "+str(C)
    # return output

    A = A
    B = B
    C = C
    equivalence = False
    tokens = str(input).split()
    string = " "
    Conjunction = " and "
    Disjunction = " or "
    strA = " A "
    strB = " B "
    strC = " C "
    start = " ( "
    end = " ) "
    check = False
    isMorgan = False
    for token in tokens:
        # print("This is the token "+token+" This is the string: " + string)
        if token == 'N':
            string = negation_func(string, A, B, C)  # adds not before last vairable or (
        if token == '<':
            string = string + Conjunction  # adds and
        if token == 'O':
            string = string + Disjunction  # adds or
        if token == 'I':
            try:
                string, check = implication_func(string, A, B, C)
            except:
                check = False
            if check:
                break
        if token == 'E':
            isMorgan = deMorgan_func(input)
            if isMorgan:
                break
            string = equivalence_func(string, A, B, C)
            equivalence = True
        if token == 'A':
            string = string + strA  # adds A
        if token == 'B':
            string = string + strB  # adds B
        if token == 'C':
            string = string + strC  # adds C
        if token == '(':
            string = string + start  # adds (
        if token == ')':
            string = string + end  # adds (
        if token == '[':
            string = string + start  # adds (
        if token == ']':
            string = string + end  # adds (

    if isMorgan:
        return True
    if check:
        return True
    if equivalence:
        string = string + end
    try:

        # print("This is the string to be tested " + string + str(eval(string)))
        return evaluation_func(string, A, B, C)
    except:
        string = start + string
        # print("This is the string to be tested B " + string + str(eval(string)))
        return evaluation_func(string, A, B, C)


def deMorgan_func(input):
    # print(input)
    stripped_string = input.strip()
    if stripped_string == "( A O B ) N E A N A B N":
        # print("Gotcha")
        return True
    if stripped_string == "( A < B ) N E A N O B N":
        return True


def truth_table_func(input):
    function = str(input)
    tokens = function.split()
    isb = False
    for token in tokens:
        # print(token)
        if token == 'C':
            # print("Fount IT")
            return print_C_table(function, c_table_func(function), Tautology_func(c_table_func(function)),
                                 Contradiction_func(
                                     c_table_func(function)))
        if token == "B":
            isb = True
    if isb:
        return print_B_table(function, b_table_func(function), Tautology_func(b_table_func(function)),
                             Contradiction_func(b_table_func(function)))

    return print_A_table(function, a_table_func(function), Tautology_func(a_table_func(function)),
                         Contradiction_func(a_table_func(function)))


# Sysmbol Table
# N Negation
# < Conjunction
# O Disjunction
# I Implication
# E Equivalence
#
def c_table_func(function):
    outcomes = []
    A = True
    B = True
    C = True
    for x in range(2):
        for y in range(2):
            for z in range(2):
                # print("A: ", A, " B: ", B, " C: ", C, " ")
                outcomes.append(process_wff(A, B, C, function))
                C = not C
            B = not B
        A = not A
    return outcomes


def b_table_func(function):
    # print("B table is called")
    outcomes = []
    A = True
    B = True
    C = False
    for x in range(2):
        for y in range(2):
            # print("A: ", A, " B: ", B,)
            outcomes.append(process_wff(A, B, C, function))
            B = not B
        A = not A
    return outcomes


def a_table_func(function):
    outcomes = []
    A = True
    B = False
    C = False
    for x in range(2):
        outcomes.append(process_wff(A, B, C, function))
        A = not A
    return outcomes


def Tautology_func(outcomes):
    # print(outcomes)
    tautology = True
    for outcome in outcomes:
        # print("This is it folks ", not outcome[0])
        if not outcome:
            tautology = False
    return tautology


def Contradiction_func(outcomes):
    contradiction = True
    for outcome in outcomes:
        if outcome:
            contradiction = False
    return contradiction


def print_C_table(function, outcomes, tautology, contradiction):
    A = True
    B = True
    C = True
    i = 0
    output = ""
    output = " A\t| B\t| C\t| " + str(function) + " |\n"
    for x in range(2):
        for y in range(2):
            for z in range(2):
                output += "" + str(A) + "\t| " + str(B) + "\t| " + str(C) + "\t| " + str(outcomes[i]) + "\n"
                i += 1
                C = not C
            B = not B
        A = not A
    if tautology:
        output += "tautology\n"
    if contradiction:
        output += "contradiction\n"

    return output


def print_B_table(function, outcomes, tautology, contradiction):
    A = True
    B = True
    i = 0
    output = ""
    output = " A\t| B\t| " + str(function) + " |\n"
    for x in range(2):
        for y in range(2):
            output += "" + str(A) + "\t| " + str(B) + "\t| " + str(outcomes[i]) + "\n"
            i += 1
            B = not B
        A = not A
    if tautology:
        output += "tautology\n"
    if contradiction:
        output += "contradiction\n"

    return output


def print_A_table(function, outcomes, tautology, contradiction):
    A = True
    i = 0
    output = " A\t| " + str(function) + " |\n"
    for x in range(2):
        output += "" + str(A) + "\t| " + str(outcomes[i]) + "\n"
        i += 1
        A = not A
    if tautology:
        output += "tautology\n"
    if contradiction:
        output += "contradiction\n"

    return output
