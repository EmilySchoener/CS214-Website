import wff


def print_C_table(function, outcomes, tautology, contradiction):
    A = True
    B = True
    C = True
    i = 0
    output=""
    output=(" A\t\t| B\t\t\t| C\t\t\t| ", function, " |\n")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                output+=("", A, "\t| ", B, "\t| ", C, "\t| ", outcomes[i])
                i += 1
                C = not C
            B = not B
        A = not A
    if tautology:
        print("tautology")
    if contradiction:
        print("contradiction")

    print(output)

def print_B_table(function, outcomes, tautology, contradiction):
    A = True
    B = True
    i = 0
    print(" A\t\t| B\t\t\t| ", function, " | ")
    for x in range(2):
        for y in range(2):
            print("", A, "\t| ", B, "\t| ", outcomes[i])
            i += 1
            B = not B
        A = not A
    if tautology:
        print("tautology")
    if contradiction:
        print("contradiction")


def print_A_table(function, outcomes, tautology, contradiction):
    A = True
    i = 0
    print(" A\t\t| ", function, " | ")
    for x in range(2):
        print("", A, "\t| ", outcomes[i])
        i += 1
        A = not A
    if tautology:
        print("tautology")
    if contradiction:
        print("contradiction")


# Sysmbol Table
# N Negation
# < Conjunction
# O Disjunction
# I Implication
# E Equivalence
#

# question 3
print("************** Question 3 **************")
A = True
B = False
C = True
print("A: ", A, "B ", B, "C ", C)
# a
print("a")
input = "A  < ( B O C ) "
print(input)
print(wff.wff_string_return_bool(A, B, C, input))
print()
# b
print("b")
input = "( A < B ) O C "
print(input)
print(wff.wff_string_return_bool(A, B, C, input))
print()
# c
print("c")
input = "( A < B ) N O C "
print(input)
print(wff.wff_string_return_bool(A, B, C, input))
print()
# d
print("d")
input = "A N O ( B N < C ) N "
print(input)
print(wff.wff_string_return_bool(A, B, C, input))
print()
print("*****************************************")
print()
print()

# Sysmbol Table
# N Negation
# < Conjunction
# O Disjunction
# I Implication
# E Equivalence

#question 4
print("************** Question 4 **************")
A = False
B = True
C = True
print("A: ", A, "B ", B, "C ", C)
# a
print("a")
input = " A I ( B O C ) "
print(input)
print(wff.wff_string_return_bool(A, B, C, input))
print()
# b
print("b")
input = " ( A O B ) I C "
print(input)
print(wff.wff_string_return_bool(A, B, C, input))
print()
# c
print("C")
input = " C I ( A N < B N ) "
print(input)
print(wff.wff_string_return_bool(A, B, C, input))
print()
# d
print("D")
input = " A O ( B N I C ) "
print(input)
print(wff.wff_string_return_bool(A, B, C, input))
print()
print("*****************************************")
print()
print()

# question 7
print("************** Question 7 **************")
print("A")
input = "Either A or B"
print(wff.convert(input))
print()

print("B")
input = "Neither A nor B"
print(wff.convert(input))
print()
print("*****************************************")
print()
print()

# question 23
print("************** Question 23 **************")

print("a")
input="( A I B ) E A N O B "
outputs, tautology,contradiction=wff.truth_table_func(input)
print_B_table(input, outputs,tautology,contradiction)

print()
print()

print("b")
input="( ( A < B ) O C ) I ( A < ( B O C ) )"
outputs, tautology,contradiction =wff.truth_table_func(input)
print_C_table(input, outputs,tautology,contradiction)

print("c")
input=" A < ( A N O B N ) N "
outputs, tautology,contradiction=wff.truth_table_func(input)
print_B_table(input, outputs,tautology,contradiction)

print("d")
input=" A < B I A N "
outputs, tautology,contradiction=wff.truth_table_func(input)
print_B_table(input, outputs,tautology,contradiction)
#
print("e")
input="( A I B ) I [ ( A O B ) I ( B O C ) ] "
outputs, tautology,contradiction =wff.truth_table_func(input)
print_C_table(input, outputs,tautology,contradiction)

print("*****************************************")
print()
print()


print("************** Question 24 **************")
print("a")
input = " A I ( B I A ) "
outputs, tautology, contradiction = wff.truth_table_func(input)
print("This is the output, ",outputs)
print(tautology," ", contradiction)
print_B_table(input, outputs, tautology, contradiction)

print("b")
input = " A < B E B N O A N "
outputs, tautology, contradiction = wff.truth_table_func(input)

print_B_table(input, outputs, tautology, contradiction)
print("c")
input = " ( A O B N ) < ( A < B ) N "
outputs, tautology, contradiction = wff.truth_table_func(input)
print_B_table(input, outputs, tautology, contradiction)
print("d")
input=" [ ( A O B ) < C N ] I A N O C  "
outputs, tautology,contradiction =wff.truth_table_func(input)
print_C_table(input, outputs,tautology,contradiction)
print("e")
input=" A N I ( B O C N ) "
outputs, tautology,contradiction =wff.truth_table_func(input)
print_C_table(input, outputs,tautology,contradiction)
print("*****************************************")
print()
print()

print("************** Question 26 **************")
print("a")
input = " A O A N "
outputs, tautology, contradiction = wff.truth_table_func(input)
print_A_table(input, outputs, tautology, contradiction)
print("b")
input = "  ( A N ) N E A "
outputs, tautology, contradiction = wff.truth_table_func(input)
print_A_table(input, outputs, tautology, contradiction)
print("c")
input = "  ( A N ) N E A "
outputs, tautology, contradiction = wff.truth_table_func(input)
print_A_table(input, outputs, tautology, contradiction)
print("d")
input = "  A < B I B "
outputs, tautology, contradiction = wff.truth_table_func(input)
print_B_table(input, outputs, tautology, contradiction)
print("e")
input = " ( A O B ) N E A N A B N "
outputs, tautology, contradiction = wff.truth_table_func(input)
print_B_table(input, outputs, tautology, contradiction)
print("f")
input = " ( A < B ) N E A N O B N "
outputs, tautology, contradiction = wff.truth_table_func(input)
print_B_table(input, outputs, tautology, contradiction)
print("g")
input = " A O A E A "
outputs, tautology, contradiction = wff.truth_table_func(input)
print_A_table(input, outputs, tautology, contradiction)
print("*****************************************")
print()
print()

print("************** Question 27 **************")
print("a")
input = " A O A N "
outputs = wff.proof_func(input)
print(outputs)
print("b")
print("c")
print("*****************************************")
print()
print()
#
# print("************** Question 28 **************")
# print("a")
# print("a")
# print("a")
# print("*****************************************")
# print()
# print()
# # Sysmbol Table
# # N Negation
# # < Conjunction
# # O Disjunction
# # I Implication
# # E Equivalence
