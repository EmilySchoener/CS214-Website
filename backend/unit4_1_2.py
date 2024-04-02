def powerSet(s, tempstring):
    if not s:
        return "{∅}"  # Return a string representation of an empty set

    element = s.pop()  # Remove an element from the set
    subsets = powerSet(s, tempstring)  # Recursively calculate the power set without the element
    subsets_with_element = []

    # Add the removed element to each subset and create new subsets
    for subset in subsets:
        subsets_with_element.append(subset)
        subsets_with_element.append(subset + ", " + str(element))

    return "{" + ", ".join(subsets_with_element) + "}"


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