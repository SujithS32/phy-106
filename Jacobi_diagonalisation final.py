import numpy as np

def tol(A):
    n = len(A)
    mu = 0
    for i in range(n-1):
        for j in range(i+1, n):
            mu += abs(A[i, j])
    mu *= 0.5 / (n * (n - 1))
    return mu

def jacobi(a, tol=1.0e-9):
    n = len(a)
    maxRot = 5 * (n**2)
    p = np.identity(n) * 1.0
    
    while True:
        mu = tol(a)
        if mu < tol:
            return np.diag(a), p
        
        changed = False
        for i in range(n-1):
            for j in range(i+1, n):
                if abs(a[i, j]) > tol:
                    changed = True
                    rotate(a, p, i, j)
        
        if not changed:
            print('Jacobi method converged')
            return np.diag(a), p
    
    print('Jacobi method did not converge')

def rotate(a, p, k, l):
    n = len(a)
    if a[k, l] == 0:
        return
    
    a_diff = a[l, l] - a[k, k]
    if abs(a[k, l]) < abs(a_diff) * 1.0e-36:
        t = a[k, l] / a_diff
    else:
        phi = a_diff / (2.0 * a[k, l])
        t = 1.0 / (abs(phi) + np.sqrt(phi**2 + 1.0))
        if phi < 0.0:
            t = -t
    c = 1.0 / np.sqrt(t**2 + 1.0)
    s = t * c
    tau = s / (1.0 + c)
    
    a[k, k] -= t * a[k, l]
    a[l, l] += t * a[k, l]
    a[k, l] = 0.0
    a[l, k] = 0.0
    
    for i in range(n):
        if i != k and i != l:
            temp = a[i, k]
            a[i, k] -= s * (a[i, l] + tau * temp)
            a[k, i] -= s * (a[l, i] + tau * a[k, i])
            a[i, l] += s * (temp - tau * a[i, l])
            a[l, i] += s * (a[k, i] - temp * tau)
        
        temp = p[i, k]
        p[i, k] -= s * (p[i, l] + tau * temp)
        p[i, l] += s * (temp - tau * p[i, l])

# Example usage:
a = np.array([[4.0, -2.0, 2.0],
              [-2.0, 2.0, -4.0],
              [2.0, -4.0, 11.0]])

lam, x = jacobi(a, tol=tol)
print("Eigenvalues:", lam)
print("Eigenvectors:", x)
