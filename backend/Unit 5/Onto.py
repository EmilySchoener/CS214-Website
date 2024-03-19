d = int(input("How many numbers are in the domain?"))
cd = int(input("How many numbers are in the co-domain?"))

Domain = [] #Domain is S
Co_Domain = [] #Codomain is T
Function = []
Onto = True

print("Enter the numbers in the domain")
for i in range (0,d):
    ele = int(input())
    Domain.append(ele)

print("Enter the numbers in the co-domain")
for i in range (0,d):
    ele = int(input())
    Co_Domain.append(ele)

n = int(input("How many pairs are in the function?"))

print("Enter pairs:")
for i in range(0,n):
    ele = [int(input()), int(input())]
    Function.append(ele)

for i in range(0,cd):
    for j in range(0,n):
        if Co_Domain[i] == Function[j][1]:
            break
        elif (j+1) == n:
            Onto = False
            break
    if not Onto:
        break

if Onto:
    print("The function is Onto")
if not Onto:
    print("The function is not Onto")

