import numpy as np


def matrix_mult(A, B):
    C = np.matmul(A, B)
    return C

def matrix_mult_reverse(B, A):
    C = np.matmul(B, A)
    return C

def matrix_and(A, B):
    #C = []
    n = len(A)
    p = len(B[0])
    m = len(A[0])
    C = [[0]*p for _ in range(n)]
    for i in range (n):
        for j in range (p):
            if A[i][j] == 1 and B[i][j] == 1:
                C[i][j] = 1
            elif A[i][j] == 0 and B[i][j] == 0:
                C[i][j] = 0

    return C

def matrix_or(A, B):
    #C = []
    n = len(A)
    p = len(B[0])
    m = len(A[0])
    C = [[0]*p for _ in range(n)]
    for i in range (n):
        for j in range (p):
            if A[i][j] == 1 or B[i][j] == 1:
                C[i][j] = 1
            else:
                C[i][j] = 0

    return C

def matrix_dot(A, B):
    C = np.dot(A,B)

    return C


#matrix1 = [[1,0,0],[1,0,0],[1,0,0]]
#matrix2 = [[1,0,0],[0,0,0],[1,0,0]]
