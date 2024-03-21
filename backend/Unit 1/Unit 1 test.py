import wff

#Sysmbol Table
#N Negation
#< Conjunction
#O Disjunction
#I Implication
#E Equivalence
#

# question 3
print("Question 3")
A = True
B = False
C = True
print("A: ", A,"B ", B,"C ",C)
#a
print("A")
input = "A  < ( B O C ) "
wff.wff_string_return_bool(A,B,C, input)
print()
#b
print("B")
input = " ( A < B ) O C "
wff.wff_string_return_bool(A,B,C, input)
print()
#c
print("C")
input = " ( A < B ) N O C "
wff.wff_string_return_bool(A,B,C, input)
print()
#d
print("D")
input = " A N O ( B N < C ) N "
wff.wff_string_return_bool(A,B,C, input)
print()


#Sysmbol Table
#N Negation
#< Conjunction
#O Disjunction
#I Implication
#E Equivalence
#
# question 4
print("Question 4")
A = False
B = True
C = True
print("A: ", A,"B ", B,"C ",C)
#a
print("A")
input = " A I ( B O C ) "
wff.wff_string_return_bool(A,B,C, input)
print()
#b
print("B")
input = " ( A O B ) I C "
#wff.wff_string_return_bool(A,B,C, input)
print()
#c
print("C")
input = " C I ( A N < B N ) "
#wff.wff_string_return_bool(A,B,C, input)
print()
#d
print("D")
input = " A O ( B N I C ) "
#wff.wff_string_return_bool(A,B,C, input)
print()

# question 7
print("Question 7")
print("A")
input = "Either A or B"
print(wff.convert(input))
print()

print("B")
input = "Neither A nor B"
print(wff.convert(input))
print()

# question 23