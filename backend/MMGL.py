import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

#random.seed(0)
#np.random.seed(0)
'''
n = int(input("Enter the number of characters in S: "))
S = []
#Hasse = nx.Graph()
p = []
minimal = True
maximal = False


print("Enter characters in S: ")
for i in range(0,n):
    ele = input()
    S.append(ele)


#for i in range(0,n):
   # Hasse.add_node(S[i])

m = int(input("Enter the number of pairs in the partial ordering: "))


print("Enter the coordinate pairs in the partial ordering: ")
for i in range(0,m):
    ele = [input(), input()]
    p.append(ele)

#for i in range(0,m):
#  Hasse.add_edge(p[i][0],p[i][1])
'''
def MMGL(S, p):
    minimal_elements = []
    maximal_elements = []
    #print(S)
    #print(p)
    ordering_string = []
    minimal = True
    maximal = False
    for i in range(0,len(S)):
     for j in range (0,len(p)):
        if S[i] == p[j][0] and S[i] == p[j][1]:
            continue
        if S[i] == p[j][0] and S[i] != p[j][1]:
            minimal = True
            maximal = False
            break
        if S[i] != p[j][0] and S[i] != p[j][1]:
            minimal = True
            maximal = True
            continue
        elif S[i] != p[j][0] and p[j][0] != p[j][1]:
            maximal = True
            minimal = False
            break

     if minimal and maximal:
        ordering_string.append(f"The element {S[i]} is a maximal and minimal element in the partial ordering")
        maximal = False
        continue
     if minimal:
         ordering_string.append(f"The element {S[i]} is a minimal element in the partial ordering")
         minimal_elements.append(S[i])
     if not minimal:
        ordering_string.append(f"The element {S[i]} is a maximal element in the partial ordering")
        maximal_elements.append(S[i])

    least_element = min(minimal_elements) if minimal_elements else None
    greatest_element = max(maximal_elements) if maximal_elements else None

    if least_element:
        ordering_string.append(f"The least element is {least_element}")
    if greatest_element:
        ordering_string.append(f"The greatest element is {greatest_element}")

    return ordering_string

#S = ['A', 'B', 'C']
#p = [['A', 'B'], ['B', 'C']]
#print(MMGL(S, p))




