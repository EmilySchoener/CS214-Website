import wff

test = wff.WFF()
test2 = wff.Truth_Table()
output = ""

# question 3
print("************** Question 3 **************")
A = True
B = False
C = True
test.set_letters(A, B, C)
print("A: ", A, "B ", B, "C ", C)
# a
print("a")
input = "A  & ( B * C ) "
print(input)
output = test.parser_adv(input)
print(output)
print()
# b
print("b")
input = "( A & B ) * C "
print(input)
output = test.parser_adv(input)
print(output)
print()
# c
print("c")
input = "( A & B ) ' * C "
print(input)
output = test.parser_adv(input)
print(output)
print()
# d
print("d")
input = "A ' * ( B ' & C ) ' "
print(input)
output = test.parser_adv(input)
print(output)
print()
print("*****************************************")
print()
print()

# question 4
print("************** Question 4 **************")
A = False
B = True
C = True
test.set_letters(A, B, C)
print("A: ", A, "B ", B, "C ", C)
# a
print("a")
input = " A - ( B * C ) "
print(input)
output = test.parser_adv(input)
print(output)
print()
# b
print("b")
input = " ( A * B ) - C "
print(input)
output = test.parser_adv(input)
print(output)
print()
# c
print("C")
input = " C - ( A ' & B ' ) "
print(input)
output = test.parser_adv(input)
print(output)
print()
# d
print("D")
input = " A * ( B ' - C ) "
print(input)
output = test.parser_adv(input)
print(output)
print()
print("*****************************************")
print()
print()

print(output)
# question 23
print("************** Question 23 **************")

print("a")
input = " ( A - B ) = A ' * B "
print(test2.table_creation(input))

print()
print()

print("b")
input = " ( A & B ) * C - A & ( B * C ) "
print(test2.table_creation(input))

print()
print()

print("c")
input = " A & ( A ' * B ' ) ' "
print(test2.table_creation(input))

print()
print()

print("d")
input = " A & B - A ' "
print(test2.table_creation(input))

print()
print()
#
print("e")
input = " ( A - B ) - [ ( A * C ) - ( B * C ) ] "
print(test2.table_creation(input))

print()
print()

print("*****************************************")

print()
print()

print("************** Question 24 **************")
print("a")
input = " A - ( B - A ) "
print(test2.table_creation(input))
print()
print()

print("b")
input = " A & B = B ' * A ' "
print(test2.table_creation(input))
print()
print()


print("c")
input = " ( A * B ' ) & ( A & B ) ' "
print(test2.table_creation(input))
print()
print()

print("d")
input = " [ ( A * B ) & C ' ] - A ' * C "
print(test2.table_creation(input))
print()
print()

print("e")
input = " A ' - ( B * C ' ) "
print(test2.table_creation(input))
print()
print()

print("*****************************************")
print()
print()


print("************** Question 26 **************")
print("a")
input = " A * A '"
print(test2.table_creation(input))
print()
print()

print("b")
input = "( A ' ) ' = A  "
print(test2.table_creation(input))
print()
print()


print("c")
input = " A & B - B"
print(test2.table_creation(input))
print()
print()


print("d")
input = " A - A * B"
print(test2.table_creation(input))
print()
print()


print("e")
input = " ( A * B ) ' = A ' & B ' "
print(test2.table_creation(input))
print()
print()


print("f")
input = " ( A & B ) ' = A ' * B ' "
print(test2.table_creation(input))
print()
print()


print("g")
input = " A * A = A "
print(test2.table_creation(input))
print()
print()


print("*****************************************")
print()
print()

# print("************** Question 27 **************")
# print("a")
# input = " ( A & B ) & C = ( A & C ) & B  "
# print(test.tautology_proof(input))
# print()
# print()
# print("b")
# print("c")
# print("*****************************************")
# print()
# print()
#
# print("************** Question 28 **************")
# print("a")
# print("a")
# print("a")
# print("*****************************************")
# print()
# print()
# # # Sysmbol Table
# # # N Negation
# # # < Conjunction
# # # O Disjunction
# # # I Implication
# # # E Equivalence


# def print_C_table(function, outcomes, tautology, contradiction):
#     A = True
#     B = True
#     C = True
#     i = 0
#     output = ""
#     output = (" A\t\t| B\t\t\t| C\t\t\t| ", function, " |\n")
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 output += ("", A, "\t| ", B, "\t| ", C, "\t| ", outcomes[i])
#                 i += 1
#                 C = not C
#             B = not B
#         A = not A
#     if tautology:
#         print("tautology")
#     if contradiction:
#         print("contradiction")
#
#     print(output)
#
#
# def print_B_table(function, outcomes, tautology, contradiction):
#     A = True
#     B = True
#     i = 0
#     print(" A\t\t| B\t\t\t| ", function, " | ")
#     for x in range(2):
#         for y in range(2):
#             print("", A, "\t| ", B, "\t| ", outcomes[i])
#             i += 1
#             B = not B
#         A = not A
#     if tautology:
#         print("tautology")
#     if contradiction:
#         print("contradiction")
#
#
# def print_A_table(function, outcomes, tautology, contradiction):
#     A = True
#     i = 0
#     print(" A\t\t| ", function, " | ")
#     for x in range(2):
#         print("", A, "\t| ", outcomes[i])
#         i += 1
#         A = not A
#     if tautology:
#         print("tautology")
#     if contradiction:
#         print("contradiction")
