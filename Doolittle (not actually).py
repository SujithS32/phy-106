from numpy import*

X = array([[4, -2, 1],
           [-2, 4, -2],
           [1, -2, 4],], float)
Y = array([11, -16, 17], float)

n = 3
def Doolittle(X, n):
    for k in range(n-1):
        for i in range(k+1, n):
            lam = X[i, k] / X[k, k]
            for j in range(k, n): 
                X[i, j] = X[i, j] - lam * X[k, j]
            X[i,k]=lam
    return X

X=Doolittle(X,n)
Ud=copy(X)

def Fsub(X,Y,n):
    y=[]
    y.append(Y[0])
    for i in range(1,n):
        sum=0
        for j in range(0,i):
                sum += X[i, j] * y[j]
        y1 = (Y[i] - sum) 
        y.append(y1)
    y=array(y)
    return y
y=Fsub(X,Y,n)

def backsub(X, Y, n):
    x = []
    x1 = Y[n-1] / X[n-1, n-1]
    x.append(x1)
    for i in range(2, n+1):
        sum = 0
        for j in range(1, i):
            sum += X[n-i, n-j] * x[j-1]
        x1 = (Y[n-i] - sum) / X[n-i, n-i]
        x.append(x1)
    x.reverse()  
    return x
result=backsub(X,y,n)
print(result)



from copy import copy



def pivot_to_diagonal_dominance(a, seq, s, tol=1e-9):
    n = len(a)
    for k in range(n-1):
        p = int(argmax(abs(a[k:n, k])/s[k:n])) + k
        if abs(a[p, k]) < tol:
            raise ValueError('Matrix is singular')
        if p != k:
            a[[k, p]] = a[[p, k]]
            seq[[k, p]] = seq[[p, k]]
            s[[k, p]] = s[[p, k]]
    return a, seq

def Doolittle(X, n):
    seq = array(range(n))
    s = zeros(n, dtype=float)
    for i in range(n):
        s[i] = max(abs(X[i, :]))
    for k in range(n-1):
        X, seq = pivot_to_diagonal_dominance(X, seq, s)
        for i in range(k+1, n):
            lam = X[i, k] / X[k, k]
            for j in range(k, n): 
                X[i, j] = X[i, j] - lam * X[k, j]
            X[i, k] = lam
    return X, seq

X, seq = Doolittle(X, n)
Ud = copy(X)

def Fsub(X, Y, n):
    y = []
    y.append(Y[0])
    for i in range(1, n):
        sum = 0
        for j in range(0, i):
            sum += X[i, j] * y[j]
        y1 = (Y[i] - sum) 
        y.append(y1)
    y = array(y)
    return y

y = Fsub(X, Y, n)

def backsub(X, Y, n):
    x = []
    x1 = Y[n-1] / X[n-1, n-1]
    x.append(x1)
    for i in range(2, n+1):
        sum = 0
        for j in range(1, i):
            sum += X[n-i, n-j] * x[j-1]
        x1 = (Y[n-i] - sum) / X[n-i, n-i]
        x.append(x1)
    x.reverse()  
    return x

result = backsub(X, y, n)
print(result)


import numpy as np

def DOOLITTLE(X, n):


  L = np.zeros((n, n))  # Initialize L to zero matrix
  U = np.copy(X)  # Copy X to U to preserve original matrix

  for k in range(n - 1):
    for i in range(k + 1, n):
      lam = U[i, k] / U[k, k]
      L[i, k] = lam
      for j in range(k, n):
        U[i, j] = U[i, j] - lam * U[k, j]

  # Set diagonal elements of L to 1
  for i in range(n):
    L[i, i] = 1

  return L, U

# Example usage
X = np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]], float)
n = 3

L, U = Crout(X.copy(), n)

print("Lower triangular matrix (L):")
print(L)

print("\nUpper triangular matrix (U):")
print(U)