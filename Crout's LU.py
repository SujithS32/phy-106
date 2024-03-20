import numpy as np

def Crout(X, n):


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