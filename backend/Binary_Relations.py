#n = int(input("Enter number of pairs in S:"))

#S = []
#S_unique = []

#pairs = 0
#reflexive_pairs = 0

#reflexive = True
#symmetric = True
#antisymmetric = True
#transitive = False


#print("Enter pairs:")
#for i in range(0,n):
   # ele = [int(input()), int(input())]
   # S.append(ele)
   # pairs += 1

#u = int(input("How many unique numbers are in S?"))
#print("Enter unique values")
#for i in range (0,u):
    #ele = int(input())
    #S_unique.append(ele)

def reflexive_rel(S, initialSet):
    reflexive = True
    reflexive_pairs = 0
    unique_data = set(x for l in S for x in l)
    unique_data = list(unique_data)
    print(unique_data)
    initialSet.sort()
    print(initialSet)
    if unique_data != initialSet:
        reflexive = False
        return reflexive
    for i in range (0, len(S)):
        if S[i][0] == S[i][1]:
            reflexive_pairs += 1

    if len(unique_data) == reflexive_pairs:
        return reflexive
    else:
        reflexive = False
        return reflexive

#reflexive_rel([[0,0],[1,1]], [0,1])
def irreflexive_rel(S):
    irreflexive = True
    for pair in S:
        if pair[0] == pair[1]:
            irreflexive = False
            break
    return irreflexive


def symmetric_rel(S):
    symmetric = True
    for i in range (0,len(S)):
        for j in range(0,len(S)):
            if S[i][0] == S[j][1] and S[i][1] == S[j][0]:
                break
            elif (j+1) == len(S):
                symmetric = False
                return symmetric
        if not symmetric:
            break
    return symmetric
def antisymmetric_rel(S):
    antisymmetric = True
    for i in range(len(S)):
        for j in range(len(S)):
            if S[i][0] == S[j][1] and S[i][1] == S[j][0] :
                if S[i][0] != S[j][0]:
                    antisymmetric = False
                    return antisymmetric
    return antisymmetric


#If you have (3,4) and (4,2) in the list, then (3,2) should be in the list
def transitive_rel(S):
    transitive = True
    for i in range(0,len(S)):
        for j in range(1,len(S)):
            for k in range(0,len(S)):
                if S[i][1] == S[j][0] and S[i][0] == S[k][0] and S[j][1] == S[k][1]:
                    return transitive

    transitive = False
    return transitive

#if symmetric:
    #print("The list is symmetric!")
#if not symmetric:
   # print("The list is not symmetric!")
#if transitive:
  #  print("The list is transitive!")
#if not transitive:
  #  print("The list is not transitive!")
#if antisymmetric:
   # print("The list is antisymmetric!")
#if not antisymmetric:
   # print("The list is not antisymmetric!")
