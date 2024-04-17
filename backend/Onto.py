
def onto(Domain, Co_Domain, Function):
    Onto = True
    for i in range(0,len(Co_Domain)):
        for j in range(0,len(Function)):
            if Co_Domain[i] == Function[j][1]:
             break
            elif (j+1) == len(Function):
                Onto = False
                return Onto
                #break
        if not Onto:
            break
    return Onto

#if Onto:
    #print("The function is Onto")
#if not Onto:
    #print("The function is not Onto")

