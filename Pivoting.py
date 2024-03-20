from numpy import*

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

import numpy as np

def make_diagonally_dominant(A):
  """
  Attempts to make a square matrix diagonally dominant by swapping rows,
  returning the closest configuration if exact dominance is not possible.

  Args:
      A: Square matrix.

  Returns:
      A copy of the matrix with the closest configuration to diagonal dominance,
      or None if not possible.
  """
  n = len(A)

  # Check if the matrix is square
  if n != len(A[0]):
    raise ValueError("Matrix must be square.")

  # Calculate initial dominance score
  initial_score = sum(abs(A[i, i]) - sum(abs(A[i, j]) for j in range(n) if j != i) for i in range(n))

  # Iterate through rows
  for i in range(n):
    for j in range(i + 1, n):
      # Swap rows and calculate dominance score
      A[[i, j]] = A[[j, i]]
      current_score = sum(abs(A[i, i]) - sum(abs(A[i, j]) for j in range(n) if j != i) for i in range(n))

      # Revert swap if the score doesn't improve
      if current_score <= initial_score:
        A[[i, j]] = A[[j, i]]
      else:
        initial_score = current_score

  # Return the modified matrix (or None if no improvement)
  return A.copy() if initial_score > 0 else None

# Example usage
A = np.array([[1, 2, 3], [-2, 5, 1], [4, -1, 2]], float)
dominant_A = make_diagonally_dominant(A.copy())

if dominant_A is not None:
  print("Closest configuration to diagonal dominance:")
  print(dominant_A)
else:
  print("Matrix cannot be made diagonally dominant.")





