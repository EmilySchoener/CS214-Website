import numpy as np


def matrix_mult(A, B):
    C = []
    n = len(A)
    p = len(B[0])
    m = len(A[0])
    for i in range (0,n):
        for j in range (0,p):
            C[i][j] = 0
            for k in range(0,m):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    return C

def matrix_and(A, B):
    C = []
    n = len(A)
    p = len(B[0])
    m = len(A[0])
    for i in range (0,n):
        for j in range (0,p):
            if A[i][j] == 1 and B[i][j] == 1:
                C[i][j] = 1
            else:
                C[i][j] = 0

    return C

def matrix_or(A, B):
    C = []
    n = len(A)
    p = len(B[0])
    m = len(A[0])
    for i in range (0,n):
        for j in range (0,p):
            if A[i][j] == 1 or B[i][j] == 1:
                C[i][j] = 1
            else:
                C[i][j] = 0

    return C

def matrix_dot(A, B):
    C = np.dot(A,B)

    return C