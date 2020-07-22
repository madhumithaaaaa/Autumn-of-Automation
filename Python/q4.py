import numpy as np
import random

X = np.random.normal(size=(20,20))                                               #Generating a random normalized numpy matrix of shape(20 x 20)
#print('X = ', X)

y = np.random.randint(low=-2147483648, high=2147483647, size=20, dtype='int32')  #Generating a numpy array of length 20 and data type “int32”. 
#print('y =', Y)

def matrixmult (A, B):  #Function for matrix multiplication                                                  
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
  
    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(cols_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


X_t = np.zeros((20,20)) #Initialize random matrix 

for i in range(20):     #X transpose
	for j in range(20):
		X_t[i][j] = X[j][i]
#print('X_t = ', X_t)

# FORMULA : θ = (XᵀX)^(-1) Xᵀ y

A = matrixmult(X_t, X)  
A = np.linalg.inv(A)

B = matrixmult(A, X_t)

y = y.reshape(20,1)
theta = matrixmult(B, y)
print('Theta matrix = ', theta)