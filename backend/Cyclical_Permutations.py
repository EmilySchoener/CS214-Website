'''
S = []
A = []
Cycle = []

u = int(input("How many numbers are in A?"))

print("Enter the numbers in A")
for i in range (0,u):
    ele = int(input())
    A.append(ele)

n = int(input("Enter number of pairs in S:"))

print("Enter pairs:")
for i in range(0,n):
    ele = [int(input()), int(input())]
    S.append(ele)
'''
def cycle_permutation(S):
    Cycle = [S[0][0]]

    for i in range(0,len(S)):
        for j in range (0,len(S)):
            for k in range (0,len(S)):
                if S[i][1] == S[j][0] and S[k][0] == S[j][1] and S[i][0] != S[i][1] and S[j][0] != S[j][1]:
                    ele = S[j][0]
                    if ele != Cycle[0]:
                        Cycle.append(ele)
                else:
                    continue

    return Cycle
#Issue with ordering in the for loop, may need to mess with the if statement more to get the cycle down right. Get the right numbers,
#but not 100% always in correct order
#print(Cycle)