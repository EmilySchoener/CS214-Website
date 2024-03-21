def convert(english):
    tokens = english.split()
    if tokens[0] == "Either":
        return "A or B"
    if tokens[0] == "Neither":
        return "A' and B'"

def negation_func(string):
    negation = " not "
    parts = string.split()
    last_part = parts[-1]
    if last_part == ')':

        for i in range(len(parts) - 1, -1, -1):
            if parts[i] == '(':
                index_of_opening_bracket = i
                parts.insert(index_of_opening_bracket, negation)
                break
    else:
        parts.insert(-1, negation)

    return ' '.join(parts)

def implication_func(string,A,B,C):
    start = " ( "
    end = " ) "
    conjunction = " and "
    parts = string.split()
    parts.insert(0, start)
    parts.append(end)
    FirstPart = negation_func(' '.join(parts))
    if evaluation_func(FirstPart, A,B,C,True):
        return FirstPart, True
    return FirstPart + conjunction + string, False

def evaluation_func(string, A,B,C, isAntcendent = False):
    if isAntcendent and eval(string):
        print("This is an antcendent and therefore will always be true since the hypothesis is False")
        return True
    print(string)
    return eval(string)

def wff_string_return_bool(A,B,C,input):
    A = A
    B = B
    C = C
    tokens = input.split()
    string = ""
    Conjunction = " and "
    Disjunction = " or "
    Equivalence = ""
    strA = " A "
    strB = " B "
    strC = " C "
    start = " ( "
    end = " ) "
    for token in tokens:

        if token == 'N':
            string = negation_func(string) #adds not before last vairable or (
        if token == '<':
            string = string + Conjunction #adds and
        if token == 'O':
            string = string + Disjunction #adds or
        if token == 'I':
            string, check = implication_func(string,A,B,C)
            if check:
                break
        if token == 'E':
            string = string
        if token == 'A':
            string = string + strA #adds A
        if token == 'B':
            string = string + strB #adds B
        if token == 'C':
            string = string + strC #adds C
        if token == '(':
            string = string + start #adds (
        if token == ')':
            string = string + end #adds (

    print(string)
    print(evaluation_func(string,A,B,C))
    return True

def truth_table_func(function):
    tokens = function.split()
    for token in tokens:
        if token == 'C':
            create_8_table(function)
    create_4_table(function)

def create_8_table(function):
    return 1

def create_4_table(function):
    return 1
#Sysmbol Table
#N Negation
#< Conjunction
#O Disjunction
#I Implication
#E Equivalence
#
