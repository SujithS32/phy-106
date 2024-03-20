import numpy as np


def jacobi(A, X_guess, B, n):
    norm = 1
    iter_count = 0
    while norm >= 1e-8 and iter_count < 1000:  # Add max_iter check
        iter_count += 1
        X_iterated = np.zeros_like(X_guess)
        for i in range(n):
            sum = 0
            for j in range(n):
                if j != i:
                    sum += A[i, j] * X_guess[j]
            X_iterated[i] = (1 / A[i, i]) * (B[i] - sum)
        norm = np.linalg.norm(X_iterated - X_guess) / np.linalg.norm(X_guess)
        X_guess = X_iterated

    print(f"Jacobi method converged in {iter_count} iterations.")
    return X_iterated


def gauss_seidel(A, X_guess, B, n):
    norm = 1
    iter_count = 0
    while norm >= 1e-8 and iter_count < 1000:  # Add max_iter check
        iter_count += 1
        for i in range(n):
            sum = 0
            for j in range(n):
                if j != i:
                    sum += A[i, j] * X_guess[j]
            X_guess[i] = (1 / A[i, i]) * (B[i] - sum)
        norm = np.linalg.norm(np.dot(A, X_guess) - B) / np.linalg.norm(B)

    print(f"Gauss-Seidel method converged in {iter_count} iterations.")
    return X_guess


def sor(A, X_guess, B, tol=1e-8, max_iter=1000):
    n = len(B)
    iter_count=0

    # Check for singular matrix (already included)
    if np.linalg.det(A) == 0:
        raise ValueError("Matrix A is singular. The SOR method may not converge.")

    # Calculate initial norm before updating
    norm = np.linalg.norm(np.dot(A, X_guess) - B) / np.linalg.norm(B)
    while norm > tol:
        omega=1.25

        # Update each element
        for i in range(n):
            iter_count += 1
            sum_val = 0
            for j in range(n):
                if j != i:
                    sum_val += A[i, j] * X_guess[j]
            X_guess[i] = (1 - omega) * X_guess[i] + (omega / A[i, i]) * (B[i] - sum_val)

        # Calculate new norm after update
        new_norm = np.linalg.norm(np.dot(A, X_guess) - B) / np.linalg.norm(B)
        print(f"Iteration {iter_count}: norm = {new_norm:.5e}")
        norm = new_norm

    if iter_count >= max_iter:
        print(f"Warning: Maximum number of iterations reached in SOR.")
        return None
    else:
        print(f"SOR method converged in {iter_count} iterations.")
        return X_guess

A = np.array([[4, 3, 0], [3, 4, -1], [0, -1, 4]])
X_guess = np.array([0, 0, 0], dtype=float)
B = np.array([24, 30, -24], dtype=float)

print(jacobi(A, X_guess, B, 3))
print(gauss_seidel(A, X_guess, B, 3))
print(sor(A, X_guess, B, tol=1e-6, max_iter=1000))
