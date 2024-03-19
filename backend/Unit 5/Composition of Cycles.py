import re
import functools

from sympy.combinatorics import Permutation


def compose_cycles(input_string):
    # Split the cycles by regex
    cycles = re.findall("\(([\d,]+)\)", input_string)

    # Break each cycle into a list of integers
    cycles = [list(map(int, x.split(","))) for x in cycles]

    # Make each cycle into a Sympy Permutation
    cycles = [Permutation([x]) for x in cycles]

    composition = functools.reduce(lambda x, y: y * x, cycles)
    print(composition)
    return str(composition)

S = []
n = int(input("Enter number of pairs in S:"))

print("Enter pairs:")
for i in range(0,n):
    ele = [(input()), (input()), (input()), (input())]
    S.append(ele)
#Need to find a different way to do composition of cycles, sympy does not work for user input
compose_cycles('(S)')
#compose_cycles('(1,3,4)(5,6)(2,3,5)(6,1)')