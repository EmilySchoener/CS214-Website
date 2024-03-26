d = int(input("How many numbers are in the domain?"))
cd = int(input("How many numbers are in the co-domain?"))

Domain = [] #Domain is S
Co_Domain = [] #Codomain is T
Function = []
#One_to_One = True
#counter = 0

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

def one_to_one(Domain, Co_Domain, Function):
    counter = 0
    One_to_One = True
    for i in range(0, cd):
        for j in range(0, n):
            if Co_Domain[i] == Function[j][1]:
                counter += 1
            if counter == 1:
                One_to_One = True
                return One_to_One
            elif counter > 1 or counter == 0:
                One_to_One = False
                return One_to_One
                #break
        if not One_to_One:
            break

#if One_to_One:
    #print("The function is One to One")
#if not One_to_One:
    #print("The function is not One to One")