
def one_to_one(Domain, Co_Domain, Function):
    counter = 0
    One_to_One = True
    for i in range(0, len(Co_Domain)):
        for j in range(0, len(Function)):
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
            return One_to_One
            break

#if One_to_One:
    #print("The function is One to One")
#if not One_to_One:
    #print("The function is not One to One")