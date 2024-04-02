def elementOf(set1, set2, set3, left, right):

    left = convertArray(left)

    if right == 'set1':
        right = set1
    elif right == 'set2':
        right = set2
    elif left == 'set3':
        left = set3
    else:
        right = convertArray(right)

    if len(left) > 1:
        Factor = True
        for element in left:
            if element in right:
                print("Found " + element + " in right")
            else:
                Factor = False
                return "False, did not find " + element + "in " + str(right)
        if Factor == True:
            print("True")
            return "True"
        else:
            print("False")
            return "False"
    else:
        if left[0] in right:
            print("True")
            return "True"
        else:
            return "False, " + str(left[0]) + " is not in " + str(right)
            #return "False"

def subset(set1, set2, set3, left, right):

    if left == 'set1':
        left = set1
    elif left == 'set2':
        left = set2
    elif left == 'set3':
        left = set3
    else:
        left = convertArray(left)

    if right == 'set1':
        right = set1
    elif right == 'set2':
        right = set2
    elif right == 'set3':
        right = set3
    else:
        right = convertArray(right)

    if len(left) > 1:
        for element in left:
            if element in right:
                print("Found " + element + " in right")
            else:
                return "False, did not find " + element + " in " + str(right)

        return "True"

    else:
        if left[0] in right:
            return "True"
        else:
            return "False, " + str(left[0]) + " is not in " + str(right)

def properSubset(set1, set2, set3, left, right):
    if left == 'set1':
        left = set1
    elif left == 'set2':
        left = set2
    elif left == 'set3':
        left = set3
    else:
        left = convertArray(left)

    if right == 'set1':
        right = set1
    elif right == 'set2':
        right = set2
    elif right == 'set3':
        right = set3
    else:
        right = convertArray(right)

    if len(left) > 1:
        for element in left:
            if element not in right:
                return f"False, {left} is not a proper subset of {right}, no {element} found."
        if len(left) < len(right):
            return f"True, {left} is a proper subset of {right}."
        else:
            return f"False, {left} is not a proper subset of {right} because it has the same or more elements."
    else:
        if left[0] in right and len(left) < len(right):
            return f"True, {left[0]} is in {right} and {left[0]} is a proper subset of {right}."
        else:
            return f"False, {left[0]} was not found in {right} or it has the same or more elements."


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



