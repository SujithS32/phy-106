import numpy as np

def cholesky(A):
    n = len(A)
    L = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i+1):
            sum_val = 0
            for k in range(j):
                sum_val += L[i, k] * L[j, k]
                
            if i == j:
                L[i, j] = np.sqrt(A[i, j] - sum_val)
            else:
                L[i, j] = (A[i, j] - sum_val) / L[j, j]

    return L


def Fsub(X, Y, n):
    y = np.zeros(n)
    y[0] = Y[0] / X[0, 0]
    for i in range(1, n):
        sum = 0
        for j in range(i):
            sum += X[i, j] * y[j]
        y[i] = (Y[i] - sum) / X[i, i]
    return y


def backsub(X, Y, n):
    x = np.zeros(n)
    x[n-1] = Y[n-1] / X[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += X[i, j] * x[j]
        x[i] = (Y[i] - sum) / X[i, i]
    return x


A = np.array([[1,1,-1],
              [1,2,0],
              [-1,0,5]], float)
b = np.array([0,5,14], float)
n=3
L = cholesky(A)
U = L.T  

y = Fsub(L, b, n)
x = backsub(U, y, n)

print("Solution:", x)






