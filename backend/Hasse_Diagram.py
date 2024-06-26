import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

'''
n = int(input("Enter the number of characters in S: "))
S = []
p = []
minimal = True
maximal = False


print("Enter characters in S: ")
for i in range(0,n):
    ele = input()
    S.append(ele)


for i in range(0,n):
    Hasse.add_node(S[i])

m = int(input("Enter the number of pairs in the partial ordering: "))


print("Enter the coordinate pairs in the partial ordering: ")
for i in range(0,m):
    ele = [input(), input()]
    p.append(ele)

for i in range(0,m):
  Hasse.add_edge(p[i][0],p[i][1])

'''
def Hasse_Diagram(p):
    random.seed(0)
    np.random.seed(0)
    Hasse = nx.Graph()
    unique_data = list(x for l in p for x in l)
    for i in range(0, len(unique_data)):
        Hasse.add_node(unique_data[i])

    for i in range(0, len(p)):
        Hasse.add_edge(p[i][0], p[i][1])

    nx.draw(Hasse, with_labels=True, node_color="red", node_size=3000, font_color="white", font_size=20,
            font_family="Times New Roman", font_weight="bold", width=5)
    plt.margins(0.2)
    # plt.show()
    plt.savefig('Hasse.png')
    return 'Hasse.png'


#b = [['A','B'],['B','C']]
#Hasse_Diagram(b)
'''
for i in range(0,n):
    for j in range (0,m):
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
        print("The element", S[i], "is a maximal and minimal element in the partial ordering")
        maximal = False
        continue
    if minimal:
        print("The element", S[i], "is a minimal element in the partial ordering")
    if not minimal:
        print("The element", S[i], "is a maximal element in the partial ordering")

'''
