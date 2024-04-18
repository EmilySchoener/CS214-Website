def ThreeByThree(oneOne, oneTwo, oneThree, twoOne, twoTwo, twoThree, threeOne, threeTwo, threeThree):
    # Convert the input parameters to a 3x3 matrix
    matrix = [[int(oneOne), int(oneTwo), int(oneThree)],
              [int(twoOne), int(twoTwo), int(twoThree)],
              [int(threeOne), int(threeTwo), int(threeThree)]]

    matrixElementsSquared = [[matrix[i][j] * matrix[i][j] for j in range(3)] for i in range(3)]
    formatted_output = "A^(2) = \n"
    for row in matrixElementsSquared:
        formatted_output += "\t".join(map(str, row)) + "\n"

    matrixSquared = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # Perform matrix multiplication (square)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matrixSquared[i][j] += matrix[i][k] * matrix[k][j]

    formatted_output += "\nA^2 = \n"
    for row in matrixSquared:
        formatted_output += "\t".join(map(str, row)) + "\n"

    return formatted_output


def FourByFour(oneOne, oneTwo, oneThree,oneFour, twoOne, twoTwo, twoThree,twoFour, threeOne, threeTwo, threeThree, threeFour, fourOne, fourTwo, fourThree, fourFour):
    # Convert the input parameters to a 3x3 matrix
    matrix = [[int(oneOne), int(oneTwo), int(oneThree), int(oneFour)],
              [int(twoOne), int(twoTwo), int(twoThree), int(twoFour)],
              [int(threeOne), int(threeTwo), int(threeThree), int(threeFour)],
              [int(fourOne), int(fourTwo), int(fourThree), int(fourFour)]]

    matrixElementsSquared = [[matrix[i][j] * matrix[i][j] for j in range(4)] for i in range(4)]
    formatted_output = "A^(2) = \n"
    for row in matrixElementsSquared:
        formatted_output += "\t".join(map(str, row)) + "\n"

    matrixSquared = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # Perform matrix multiplication (square)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                matrixSquared[i][j] += matrix[i][k] * matrix[k][j]

    formatted_output += "\nA^2 = \n"
    for row in matrixSquared:
        formatted_output += "\t".join(map(str, row)) + "\n"

    return formatted_output


