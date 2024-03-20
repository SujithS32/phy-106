import numpy as np

def is_orthogonal(A, tol=1e-6):
  """
  Checks if a matrix is orthogonal.

  Args:
    A: A numpy array representing the matrix.
    tol: Tolerance for floating-point comparisons.

  Returns:
    True if the matrix is orthogonal, False otherwise.
  """

  # Check if the matrix is square
  if A.shape[0] != A.shape[1]:
    return False

  # Method 1: Multiply by transpose
  A_transpose = A.T
  result = np.dot(A, A_transpose)
  if not np.allclose(result, np.eye(A.shape[0]), atol=tol):
    return False

  # Method 2: Check dot product of columns
  for i in range(A.shape[1]):
    for j in range(i + 1, A.shape[1]):
      dot_product = np.dot(A[:, i], A[:, j])
      if abs(dot_product - 1) > tol:
        return False

  return True

# Example usage
A = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])

if is_orthogonal(A):
  print("Matrix is orthogonal")
else:
  print("Matrix is not orthogonal")
