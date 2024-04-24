def ThreeByThree(oneOne, oneTwo, oneThree, twoOne, twoTwo, twoThree, threeOne, threeTwo, threeThree):
    # string to int
    oneOne = int(oneOne)
    oneTwo = int(oneTwo)
    oneThree = int(oneThree)
    twoOne = int(twoOne)
    twoTwo = int(twoTwo)
    twoThree = int(twoThree)
    threeOne = int(threeOne)
    threeTwo = int(threeTwo)
    threeThree = int(threeThree)

    #each element of result
    b11 = oneOne * oneOne + oneTwo * twoOne + oneThree * threeOne
    b12 = oneOne * oneTwo + oneTwo * twoTwo + oneThree * threeTwo
    b13 = oneOne * oneThree + oneTwo * twoThree + oneThree * threeThree
    b21 = twoOne * oneOne + twoTwo * twoOne + twoThree * threeOne
    b22 = twoOne * oneTwo + twoTwo * twoTwo + twoThree * threeTwo
    b23 = twoOne * oneThree + twoTwo * twoThree + twoThree * threeThree
    b31 = threeOne * oneOne + threeTwo * twoOne + threeThree * threeOne
    b32 = threeOne * oneTwo + threeTwo * twoTwo + threeThree * threeTwo
    b33 = threeOne * oneThree + threeTwo * twoThree + threeThree * threeThree

    # bool elements
    b11 = bool(b11)
    b11 = 1 if b11 else 0

    b12 = bool(b12)
    b12 = 1 if b12 else 0

    b13 = bool(b13)
    b13 = 1 if b13 else 0

    b21 = bool(b21)
    b21 = 1 if b21 else 0

    b22 = bool(b22)
    b22 = 1 if b22 else 0

    b23 = bool(b23)
    b23 = 1 if b23 else 0

    b31 = bool(b31)
    b31 = 1 if b31 else 0

    b32 = bool(b32)
    b32 = 1 if b32 else 0

    b33 = bool(b33)
    b33 = 1 if b33 else 0


    # Return the resulting matrix as a list
    return f"A^(2) or (AxA) = \n{b11} {b12} {b13}\n{b21} {b22} {b23}\n{b31} {b32} {b33}"


def FourByFour(oneOne, oneTwo, oneThree,oneFour, twoOne, twoTwo, twoThree,twoFour, threeOne, threeTwo, threeThree, threeFour, fourOne, fourTwo, fourThree, fourFour):
    oneOne = int(oneOne)
    oneTwo = int(oneTwo)
    oneThree = int(oneThree)
    oneFour = int(oneFour)
    twoOne = int(twoOne)
    twoTwo = int(twoTwo)
    twoThree = int(twoThree)
    twoFour = int(twoFour)
    threeOne = int(threeOne)
    threeTwo = int(threeTwo)
    threeThree = int(threeThree)
    threeFour = int(threeFour)
    fourOne = int(fourOne)
    fourTwo = int(fourTwo)
    fourThree = int(fourThree)
    fourFour = int(fourFour)

    # Compute each element of the resulting matrix
    b11 = oneOne * oneOne + oneTwo * twoOne + oneThree * threeOne + oneFour * fourOne
    b12 = oneOne * oneTwo + oneTwo * twoTwo + oneThree * threeTwo + oneFour * fourTwo
    b13 = oneOne * oneThree + oneTwo * twoThree + oneThree * threeThree + oneFour * fourThree
    b14 = oneOne * oneFour + oneTwo * twoFour + oneThree * threeFour + oneFour * fourFour
    b21 = twoOne * oneOne + twoTwo * twoOne + twoThree * threeOne + twoFour * fourOne
    b22 = twoOne * oneTwo + twoTwo * twoTwo + twoThree * threeTwo + twoFour * fourTwo
    b23 = twoOne * oneThree + twoTwo * twoThree + twoThree * threeThree + twoFour * fourThree
    b24 = twoOne * oneFour + twoTwo * twoFour + twoThree * threeFour + twoFour * fourFour
    b31 = threeOne * oneOne + threeTwo * twoOne + threeThree * threeOne + threeFour * fourOne
    b32 = threeOne * oneTwo + threeTwo * twoTwo + threeThree * threeTwo + threeFour * fourTwo
    b33 = threeOne * oneThree + threeTwo * twoThree + threeThree * threeThree + threeFour * fourThree
    b34 = threeOne * oneFour + threeTwo * twoFour + threeThree * threeFour + threeFour * fourFour
    b41 = fourOne * oneOne + fourTwo * twoOne + fourThree * threeOne + fourFour * fourOne
    b42 = fourOne * oneTwo + fourTwo * twoTwo + fourThree * threeTwo + fourFour * fourTwo
    b43 = fourOne * oneThree + fourTwo * twoThree + fourThree * threeThree + fourFour * fourThree
    b44 = fourOne * oneFour + fourTwo * twoFour + fourThree * threeFour + fourFour * fourFour

    # bool elements
    b11 = bool(b11)
    b11 = 1 if b11 else 0

    b12 = bool(b12)
    b12 = 1 if b12 else 0

    b13 = bool(b13)
    b13 = 1 if b13 else 0

    b14 = bool(b14)
    b14 = 1 if b14 else 0

    b21 = bool(b21)
    b21 = 1 if b21 else 0

    b22 = bool(b22)
    b22 = 1 if b22 else 0

    b23 = bool(b23)
    b23 = 1 if b23 else 0

    b24 = bool(b24)
    b24 = 1 if b24 else 0

    b31 = bool(b31)
    b31 = 1 if b31 else 0

    b32 = bool(b32)
    b32 = 1 if b32 else 0

    b33 = bool(b33)
    b33 = 1 if b33 else 0

    b34 = bool(b34)
    b34 = 1 if b34 else 0

    b41 = bool(b41)
    b41 = 1 if b41 else 0

    b42 = bool(b42)
    b42 = 1 if b42 else 0

    b43 = bool(b43)
    b43 = 1 if b43 else 0

    b44 = bool(b44)
    b44 = 1 if b44 else 0

    # Return the resulting matrix as a string
    return f"A^(2) or (AxA) = \n{b11} {b12} {b13} {b14}\n{b21} {b22} {b23} {b24}\n{b31} {b32} {b33} {b34}\n{b41} {b42} {b43} {b44}"


