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


#S = input("Enter the cycles, with commas separating different functions: ")


#compose_cycles(S)