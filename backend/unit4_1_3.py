def testMatrix(set, oneOne, oneTwo, oneThree, twoOne, twoTwo, twoThree, threeOne, threeTwo, threeThree):
    # Check if each element is in the set
    elements = [oneOne, oneTwo, oneThree, twoOne, twoTwo, twoThree, threeOne, threeTwo, threeThree]
    for element in elements:
        if element not in set:
            return "False, did not find " + element + " in set"
    return "True, found every element in the matrix inside of the set" + str(set)