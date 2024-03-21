def elementOf(set1, set2, left, right):
    if left == 'set1':
        left = set1
    elif left == 'set2':
        left = set2
    else:
        left = convertArray(left)
        #print("normal number")

    if right == 'set1':
        right = set1
    elif right == 'set2':
        right = set2
    else:
        right = convertArray(right)
        #print("normal number")

    if len(left) > 1:
        Factor = True
        for element in left:
            if element in right:
                print("Found " + element + " in right")
            else:
                Factor = False
                print("Did not find " + element + "in " + str(right))
        if Factor == True:
            print("True")
        else:
            print("False")
    else:
        if left[0] in right:
            print("True")
        else:
            print("False, " + str(left[0]) + " is not in " + str(right))

def subset(set1, set2, left, right):
    print("subset")

def properSubset(set1, set2, left, right):
    print("proper subset")

def convertArray(input):
    elements = []
    currentElement = ''
    braceOpen = False

    for char in input:
        if char == '{':
            braceOpen = True
        elif char == '}':
            braceOpen = False
        elif char == ',' and not braceOpen:
            if currentElement:
                elements.append(currentElement.strip())
                currentElement = ''
            continue
        currentElement += char

    if currentElement:
        elements.append(currentElement.strip())

    return elements

def main():
    # Use a breakpoint in the code line below to debug your script.
    #element of, subset of
    print('This program will determine is a statement is true or false given up to 2 sets and a statement.')
    set1 = input("Please enter in the elements of set 1 separated by a comma: ")
    set1Array = convertArray(set1)
    print(set1Array)
    print(len(set1Array))
    set2 = input("Please enter in the elements of set 2 separated by a comma: ")
    set2Array = convertArray(set2)
    print(set2Array)
    print(len(set2Array))
    findCondition = input("type 1 for element of, type 2 for subset, type 3 for proper subset: ")
    findConditionCheck = int(findCondition)
    leftCondition = input("Enter Left Side Condition. Type set1 for set 1 and set2 for set2 if you wish to use them. ")
    rightCondition = input("Enter Right Side Condition. Type set1 for set 1 and set2 for set2 if you wish to use them. ")
    if findConditionCheck == 1:
        elementOf(set1Array, set2Array, leftCondition, rightCondition)
    elif findConditionCheck == 2:
        subset(set1Array, set2Array, leftCondition, rightCondition)
    elif findConditionCheck == 3:
        properSubset(set1Array, set2Array, leftCondition, rightCondition)
    else:
        print("You did not type a valid response for findCondition")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


