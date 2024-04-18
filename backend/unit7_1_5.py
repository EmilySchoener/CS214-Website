def WarshallClosure(set, p):
    set_elements = set.split(',')
    relation_pairs = [pair.strip('()').split(',') for pair in p.split('),(')]

    # Initialize the adjacency matrix with zeros
    num_vertices = len(set_elements)
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    # Populate the adjacency matrix based on the relation
    for pair in relation_pairs:
        i = int(pair[0]) - 1  # Adjust index
        j = int(pair[1]) - 1  # Adjust index
        adj_matrix[i][j] = 1

    # Apply Warshall's algorithm to compute the transitive closure
    closure = [[adj_matrix[i][j] for j in range(num_vertices)] for i in range(num_vertices)]
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    # Convert the matrix to a string representation
    matrix_str = '\n'.join([''.join(map(str, row)) for row in closure])

    return matrix_str