import numpy as np


def matrix_mult_2x2(A, B):
    C = 1*(np.dot(A,B) > 0)
    return f" A x B = \n[{C[0][0]} {C[0][1]}]\n[{C[1][0]} {C[1][1]}]\n"

def matrix_mult_reverse_2x2(B, A):
    C = 1*(np.dot(B,A) > 0)
    return f"B x A = \n[{C[0][0]} {C[0][1]}]\n[{C[1][0]} {C[1][1]}]\n"

def matrix_and_2x2(A, B):
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

    return f"A and B = \n[{C[0][0]} {C[0][1]}]\n[{C[1][0]} {C[1][1]}]\n"

def matrix_or_2x2(A, B):
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

    return f"A or B = \n[{C[0][0]} {C[0][1]}]\n[{C[1][0]} {C[1][1]}]\n"


def matrix_mult_3x3(A, B):
    C = 1*(np.dot(A,B) > 0)
    return f"A x B = \n[{C[0][0]} {C[0][1]} {C[0][2]}]\n[{C[1][0]} {C[1][1]} {C[1][2]}]\n[{C[2][0]} {C[2][1]} {C[2][2]}]"

def matrix_mult_reverse_3x3(B, A):
    C = 1*(np.dot(B,A) > 0)
    return f"B x A = \n[{C[0][0]} {C[0][1]} {C[0][2]}]\n[{C[1][0]} {C[1][1]} {C[1][2]}]\n[{C[2][0]} {C[2][1]} {C[2][2]}]"

def matrix_and_3x3(A, B):
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

    return f"A and B = \n[{C[0][0]} {C[0][1]} {C[0][2]}]\n[{C[1][0]} {C[1][1]} {C[1][2]}]\n[{C[2][0]} {C[2][1]} {C[2][2]}]"

def matrix_or_3x3(A, B):
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

    return f"A or B = \n[{C[0][0]} {C[0][1]} {C[0][2]}]\n[{C[1][0]} {C[1][1]} {C[1][2]}]\n[{C[2][0]} {C[2][1]} {C[2][2]}]"


def matrix_mult_4x4(A, B):
    C = 1*(np.dot(A,B) > 0)
    return f"A x B = \n[{C[0][0]} {C[0][1]} {C[0][2]} {C[0][3]}]\n[{C[1][0]} {C[1][1]} {C[1][2]} {C[1][3]}]\n[{C[2][0]} {C[2][1]} {C[2][2]} {C[2][3]}]\n[{C[3][0]} {C[3][1]} {C[3][2]} {C[3][3]}]"

def matrix_mult_reverse_4x4(B, A):
    C = 1*(np.dot(B,A) > 0)
    return f"B x A = \n[{C[0][0]} {C[0][1]} {C[0][2]} {C[0][3]}]\n[{C[1][0]} {C[1][1]} {C[1][2]} {C[1][3]}]\n[{C[2][0]} {C[2][1]} {C[2][2]} {C[2][3]}]\n[{C[3][0]} {C[3][1]} {C[3][2]} {C[3][3]}]"

def matrix_and_4x4(A, B):
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

    return f"A and B = \n[{C[0][0]} {C[0][1]} {C[0][2]} {C[0][3]}]\n[{C[1][0]} {C[1][1]} {C[1][2]} {C[1][3]}]\n[{C[2][0]} {C[2][1]} {C[2][2]} {C[2][3]}]\n[{C[3][0]} {C[3][1]} {C[3][2]} {C[3][3]}]"

def matrix_or_4x4(A, B):
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

    return f"A or B = \n[{C[0][0]} {C[0][1]} {C[0][2]} {C[0][3]}]\n[{C[1][0]} {C[1][1]} {C[1][2]} {C[1][3]}]\n[{C[2][0]} {C[2][1]} {C[2][2]} {C[2][3]}]\n[{C[3][0]} {C[3][1]} {C[3][2]} {C[3][3]}]"

#matrix1 = [[1,0,0],[1,0,0],[1,0,0]]
#matrix2 = [[1,0,0],[0,0,0],[1,0,0]]
