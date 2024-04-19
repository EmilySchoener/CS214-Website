'''
n = int(input("Enter number of pairs in S:"))
#Everything in Functions but need to alter variables and such
S = []
S_reflexive_closure = []
S_symmetric_closure = []
S_transitive_closure = []

pairs = 0
reflexive_pairs = 0

symmetric_in_list = True
transitive_in_list = True
reflexive_in_list = True

print("Enter pairs:")
for i in range(0,n):
    ele = [int(input()), int(input())]
    S.append(ele)
    pairs += 1

    Some issues with the functions in regards to getting ALL pairs for closure, but input is working on website
'''

#Need to add in a set S being typed in by users

def reflexive_closure(initial_set, S):
    # Start with the original relation
    reflexive = []

    # Add reflexive pairs for each element not in the relation
    for ele in S:
        reflexive.append([ele, ele])

    return reflexive


# Original relation p
#p = [[1, 3], [3, 3], [3, 1], [2, 2], [1, 1], [1, 2]]
# Set of elements
#S = [1, 2, 3, 5, 6]
# Compute the reflexive closure
#p_reflexive = reflexive_closure(p, S)
#print("Reflexive closure:", p_reflexive)

symmetric_in_list = True
def symmetric_closure(S):
    S_symmetric_closure = []
    global symmetric_in_list
    for i in range (0,len(S)):
        for j in range(0,len(S)):
            if S[i][0] == S[j][1] and S[i][1] == S[j][0]:
                break
            elif (j+1) == len(S):
                symmetric_in_list = False
        if not symmetric_in_list:
            ele = [S[i][1], S[i][0]]
            S_symmetric_closure.append(ele)
            #S_symmetric_closure.append(S)
            symmetric_in_list = True
    return S_symmetric_closure

#p = [[1, 3], [3, 3], [3, 1], [2, 2], [1, 1], [1, 2]]
# Compute the symmetric closure
#p_symmetric = symmetric_closure(p)
#print("Symmetric closure:", p_symmetric)

#If you have (3,4) and (4,2) in the list, then (3,2) should be in the list
#For some reason with these loops, I have issues with many coordinate pairs, but with fewer it works
def transitive_closure(initial_set, S):
    S_transitive_closure = []
    for i in range(0,len(S)):
        for j in range(0,len(S)):
            for k in range(0,len(S)):
                if [S[i], S[j]] in initial_set and [S[j], S[k]] in initial_set:
                    S_pair = [S[i], S[k]]
                    if S_pair not in S_transitive_closure and S_pair not in initial_set:
                        S_transitive_closure.append(S_pair)
    return S_transitive_closure

# Original relation p
#p = [[1, 3], [3, 3], [3, 1], [2, 2], [1, 1], [1, 2]]
# Set of elements
#S = [1, 2, 3, 5, 6]
#print("Original set:", S)
#print("Transitive closure:", transitive_closure(p, S))



'''
print("The list S with a reflexive closure has the following ordered pairs: ")
m = len(S_reflexive_closure)
for i in range(0,m):
        print(S_reflexive_closure[i])

print("The list S with a symmetric closure has the following ordered pairs: ")
m = len(S_symmetric_closure)
for i in range(0,m):
        print(S_symmetric_closure[i])

print("The list S with a transitive closure has the following ordered pairs: ")
m = len(S_transitive_closure)
for i in range(0,m):
        print(S_transitive_closure[i])
        '''