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
#S_reflexive_closure = S
#S_symmetric_closure = S
#S_transitive_closure = S
reflexive_in_list = True
symmetric_in_list = True
transitive_in_list = True
def reflexive_closure(S):
    S_reflexive_closure = []
    global reflexive_in_list
   # reflexive_in_list = True
    for i in range (0, len(S)):
     for j in range(0,len(S)):
        if S[i][0] == S[j][0] and S[i][0] == S[j][1]:
            break
        elif (j+1) == len(S):
            reflexive_in_list = False
     if not reflexive_in_list:
        ele = [(S[i][0]),(S[i][0])]
        S_reflexive_closure.append(ele)
       # S_reflexive_closure.append(S)
        reflexive_in_list = True
        return S_reflexive_closure

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

#If you have (3,4) and (4,2) in the list, then (3,2) should be in the list
#For some reason with these loops, I have issues with many coordinate pairs, but with fewer it works
def transitive_closure(S):
    S_transitive_closure = []
    global transitive_in_list
    for i in range(0,len(S)):
        for j in range(1,len(S)):
            for k in range(0,len(S)):
                if S[i][1] == S[j][0] and S[i][0] == S[k][0] and S[j][1] == S[k][1]:
                 break
                elif (k + 1) == len(S) and S[i][0] != S[j][0] and S[i][1] != S[j][1]:
                    transitive_in_list = False
                    break
            if not transitive_in_list:
                ele = [S[i][0],S[j][1]]
                S_transitive_closure.append(ele)
                S_transitive_closure.append(S)
                transitive_in_list = True
                return S_transitive_closure





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