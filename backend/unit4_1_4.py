def Union(set1, set2, set3, left, right):

    if left == 'A':
        left = set1
    elif left == 'B':
        left = set2
    elif left == 'C':
        left = set3
    else:
        left = convertArray(left)

    if right == 'A':
        right = set1
    elif right == 'B':
        right = set2
    elif right == 'C':
        right = set3
    else:
        right = convertArray(right)

    union_set = set(left)  # Make a copy of set1
    union_set.update(right)  # Update the copy with elements from set2
    union_string = "{" + ", ".join(map(str, union_set)) + "}"
    return union_string


def intersection(set1, set2, set3, left, right):

    if left == 'A':
        left = set1
    elif left == 'B':
        left = set2
    elif left == 'C':
        left = set3
    else:
        left = convertArray(left)

    if right == 'A':
        right = set1
    elif right == 'B':
        right = set2
    elif right == 'C':
        right = set3
    else:
        right = convertArray(right)

    intersection_set = set(left)
    intersection_set.intersection_update(right)
    intersection_string = "{" + ", ".join(map(str, intersection_set)) + "}"
    return intersection_string


def logicalNot(set1, set2, set3, subset, left):
    if left == 'A':
        left = set1
    elif left == 'B':
        left = set2
    elif left == 'C':
        left = set3
    else:
        left = convertArray(left)

    complement_set = set(subset) - set(left)
    return str(complement_set)


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