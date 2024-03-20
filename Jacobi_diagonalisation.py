from numpy import*
from math import*
A=array(([[80,30,0]
          [30,40,0]
          [0,0,60]]),dtype=float)
def tol(A):
  n=len(a)
  for i inrange(0,n-1):
    for j in rnage(1,n-1):
      mu=(0.5*sum)/(n*(n-1))
      return mu




import numpy as np

def jacobi(a, tol=1.0e-9):
    def maxElem(a): 
        n = len(a)
        aMax = 0.0
        for i in range(n-1):
            for j in range(i+1, n):
                if abs(a[i, j]) >= aMax:
                    aMax = abs(a[i, j])
                    k = i
                    l = j
        return aMax, k, l

    def rotate(a, p, k, l):
        n = len(a)
        aDiff = a[l, l] - a[k, k]
        if abs(a[k, l]) < abs(aDiff) * 1.0e-36:
            t = a[k, l] / aDiff
        else:
            phi = aDiff / (2.0 * a[k, l])
            t = 1.0 / (abs(phi) + np.sqrt(phi**2 + 1.0))
            if phi < 0.0:
                t = -t
        c = 1.0 / np.sqrt(t**2 + 1.0)
        s = t * c
        tau = s / (1.0 + c)
        temp = a[k, l]
        a[k, l] = 0.0
        a[k, k] = a[k, k] - t * temp
        a[l, l] = a[l, l] + t * temp
        for i in range(k):
            temp = a[i, k]
            a[i, k] = temp - s * (a[i, l] + tau * temp)
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])
        for i in range(k+1, l):
            temp = a[k, i]
            a[k, i] = temp - s * (a[i, l] + tau * a[k, i])
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])
        for i in range(l+1, n):
            temp = a[k, i]
            a[k, i] = temp - s * (a[l, i] + tau * temp)
            a[l, i] = a[l, i] + s * (temp - tau * a[l, i])
        for i in range(n):
            temp = p[i, k]
            p[i, k] = temp - s * (p[i, l] + tau * p[i, k])
            p[i, l] = p[i, l] + s * (temp - tau * p[i, l])

    n = len(a)
    maxRot = 5 * (n**2)
    p = np.identity(n) * 1.0
    
    for i in range(maxRot):
        aMax, k, l = maxElem(a)
        if aMax < tol:
            return np.diag(a), p
        rotate(a, p, k, l)
    print('Jacobi method did not converge')

# Example usage:
a = np.array([[4.0, -2.0, 2.0],
              [-2.0, 2.0, -4.0],
              [2.0, -4.0, 11.0]])

lam, x = jacobi(a)
print("Eigenvalues:", lam)
print("Eigenvectors:", x)







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
    p = np.identity(n) * 1.0
    
    while True:
        mu = tol(a)
        if mu < tol:
            return np.diag(a), p
        
        for i in range(n-1):
            for j in range(i+1, n):
                if abs(a[i, j]) > tol:
                    rotate(a, p, i, j)
    
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

      
