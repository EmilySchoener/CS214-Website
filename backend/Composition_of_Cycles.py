import re
import functools

from sympy.combinatorics import Permutation


def compose_cycles(input_string, A):
    # Split the cycles by regex
    cycles = re.findall("\(([\d,]+)\)", input_string)

    if A[0] == -1:
        A = [float('-inf'), float('inf')]
    # Break each cycle into a list of integers
    cycles = [list(map(int, x.split(","))) for x in cycles]
    #print(cycles)
    unique_data = set(x for l in cycles for x in l)
    unique_data = list(unique_data)
    #print(unique_data)
    A.sort()
    #print(A)
    if unique_data != A:
        #print("The cycles entered not valid cycles on the set A ")
        if len(unique_data) > len(A) and A != [float('-inf'), float('inf')]:
            return "The cycles entered are not valid cycles on the set A "
    # Make each cycle into a Sympy Permutation
    cycles = [Permutation([x]) for x in cycles]

    composition = functools.reduce(lambda x, y: y * x, cycles)
    #print(composition)
    return str(composition)

#A = [1,2,3,4,5]
#S = input("Enter the cycles, with commas separating different functions: ")


#print(compose_cycles(S, A))
