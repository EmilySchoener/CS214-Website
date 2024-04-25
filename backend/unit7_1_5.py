def WarshallClosure(set, p):
    setElements = set.split(',')
    numElements = len(setElements)

    # Create a dictionary to map elements to indices
    element_to_index = {element: index for index, element in enumerate(setElements)}

    relation_pairs = [pair.strip('()').split(',') for pair in p.split('),(')]

    # Initialize the adjacency matrix with zeros
    adj_matrix = [[0] * numElements for _ in range(numElements)]

    # Populate the adjacency matrix based on the relation
    for pair in relation_pairs:
        element1 = pair[0]
        element2 = pair[1]
        if element1 in element_to_index and element2 in element_to_index:
            i = element_to_index[element1]
            j = element_to_index[element2]
            adj_matrix[i][j] = 1

    # Apply Warshall's algorithm to compute the transitive closure
    closure = [[adj_matrix[i][j] for j in range(numElements)] for i in range(numElements)]
    for k in range(numElements):
        for i in range(numElements):
            for j in range(numElements):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    # Convert the matrix to a string representation
    matrix_str = '\n'.join([''.join(map(str, row)) for row in closure])

    return matrix_str


'''
set_input = "0,1,2,4,6"
set_input1 = "1,2,3"
relation_input = "(0,0),(1,1),(2,2),(4,4),(6,6),(0,1),(1,2),(2,4),(4,6)"
relation_input1 = "(1,3),(3,3),(3,1),(2,2),(2,3),(1,1),(1,2)"
relation_input2 = "(1,1),(3,3),(2,2)"
relation_input3 = "(1,1),(1,2),(2,3),(3,1),(1,3)"
relation_input4 = "(1,1),(1,2),(2,3),(1,3)"

relation_input5 = "(0,1),(1,0),(2,4),(4,2),(4,6),(6,4)"
relation_input6 = "(0,1),(1,2),(0,2),(2,0),(2,1),(1,0),(0,0),(1,1),(2,2)"
relation_input7 = "(0,0),(1,1),(2,2),(4,4),(6,6),(4,6),(6,4)"
print(WarshallClosure(set_input, relation_input7))
'''