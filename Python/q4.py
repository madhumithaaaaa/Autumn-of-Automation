import numpy as np
import random

X = np.random.normal(size=(20,20))

Y = np.random.normal(size=(20,1))


def matrixmult (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print("Cannot multiply the two matrices. Incorrect dimensions.")
      return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    print(C)

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


X_t = np.zeros((20,20))

for i in range(20):
	for j in range(20):
		X_t[i][j] = X[j][i]


A = np.linalg.inv(X)
B = matrixmult(A, X_t)
theta = matrixmult(B, Y)
print(theta)