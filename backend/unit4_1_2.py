import math


def powerSet(s):
    setSize = len(s)
    pow_set_size = int(math.pow(2, setSize))
    power_set_string = []
    # Add the empty set as the first element
    power_set_string.append("{∅}")

    for counter in range(1, pow_set_size):
        subset = []
        for j in range(0, setSize):
            if (counter & (1 << j)) > 0:
                subset.append(str(s[j]))
        power_set_string.append("{" + ", ".join(subset) + "}")

    return "{" + ", ".join(power_set_string) + "}"


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
