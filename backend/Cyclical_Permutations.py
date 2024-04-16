
def cycle_permutation(A, S):
    Cycle = []

    while A:  # Continue until all elements are visited
        first_element = next(iter(A))
        Cycle.append(first_element)
        A.remove(first_element)  # Remove the current element from the set

        for pair in S:
            if pair[0] == first_element:
                first_element = pair[1]
                break

        if Cycle[0] == first_element:
            break

    return Cycle

A = [1, 2, 3, 4]
S = [(1, 2), (2, 3), (3, 4), (4, 1)]

cycle = cycle_permutation(A, S)
print(cycle)  # Output: [1, 2, 3, 4]



#Issue with ordering in the for loop, may need to mess with the if statement more to get the cycle down right. Get the right numbers,
#but not 100% always in correct order
#print(Cycle)