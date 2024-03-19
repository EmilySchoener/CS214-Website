n = int(input("Enter number of pairs in S:"))

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

#S_reflexive_closure = S
#S_symmetric_closure = S
#S_transitive_closure = S

for i in range (0, pairs):
    for j in range(0,pairs):
        if S[i][0] == S[j][0] and S[i][0] == S[j][1]:
            break
        elif (j+1) == pairs:
            reflexive_in_list = False
    if not reflexive_in_list:
        ele = [(S[i][0]),(S[i][0])]
        S_reflexive_closure.append(ele)
        reflexive_in_list = True

for i in range (0,n):
    for j in range(0,n):
        if S[i][0] == S[j][1] and S[i][1] == S[j][0]:
            break
        elif (j+1) == n:
            symmetric_in_list = False
    if not symmetric_in_list:
        ele = [S[i][1], S[i][0]]
        S_symmetric_closure.append(ele)
        symmetric_in_list = True

#If you have (3,4) and (4,2) in the list, then (3,2) should be in the list
#For some reason with these loops, I have issues with many coordinate pairs, but with fewer it works
for i in range(0,n):
    for j in range(1,n):
        for k in range(0,n):
            if S[i][1] == S[j][0] and S[i][0] == S[k][0] and S[j][1] == S[k][1]:
                break
            elif (k + 1) == n and S[i][0] != S[j][0] and S[i][1] != S[j][1]:
                transitive_in_list = False
                break
        if not transitive_in_list:
            ele = [S[i][0],S[j][1]]
            S_transitive_closure.append(ele)
            transitive_in_list = True






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