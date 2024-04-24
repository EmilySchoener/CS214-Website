'''
n = int(input("Enter the number of characters or numbers in the first partition: "))
partition_1 = []


print("Enter characters or numbers in the first partition: ")
for i in range(0,n):
    ele = input()
    partition_1.append(ele)

m = int(input("Enter the number of characters or numbers in the second partition: "))
partition_2 = []

print("Enter characters or numbers in the second partition: ")
for i in range(0, m):
    ele = input()
    partition_2.append(ele)
'''
def equivalence_relations(partition_1, partition_2, S):
    equivalence = []

    if S != partition_1 + partition_2:
        return equivalence
    for i in range(0,len(partition_1)):
        for j in range (0,len(partition_1)):
            ele = [partition_1[i], partition_1[j]]
            equivalence.append(ele)

    for i in range(0,len(partition_2)):
        for j in range (0,len(partition_2)):
            ele = [partition_2[i], partition_2[j]]
            equivalence.append(ele)

    return equivalence

def equivalence_relations_three(partition_1, partition_2, partition_3, S):
    equivalence = []

    if S != partition_1 + partition_2 + partition_3:
        return equivalence
    for i in range(0,len(partition_1)):
        for j in range (0,len(partition_1)):
            ele = [partition_1[i], partition_1[j]]
            equivalence.append(ele)

    for i in range(0,len(partition_2)):
        for j in range (0,len(partition_2)):
            ele = [partition_2[i], partition_2[j]]
            equivalence.append(ele)

    for i in range(0,len(partition_3)):
        for j in range (0,len(partition_3)):
            ele = [partition_3[i], partition_3[j]]
            equivalence.append(ele)

    return equivalence


#part1 = ['a', 'b', 'c']
#part2 = ['d','e']
#s = ['a','b','c','d','e']
#print(equivalence_relations(part1, part2, s))
#Need to add in a set S being typed in by users