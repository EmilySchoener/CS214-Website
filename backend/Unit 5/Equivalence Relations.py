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

equivalence = []

for i in range(0,n):
    for j in range (0,n):
        ele = [partition_1[i], partition_1[j]]
        equivalence.append(ele)

for i in range(0,m):
    for j in range (0,m):
        ele = [partition_2[i], partition_2[j]]
        equivalence.append(ele)

print(equivalence)