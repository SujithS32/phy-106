import numpy as np

def gi(A):
    n = len(A)
    am = np.zeros((n, 2*n))
    
    for i in range(n):
        for j in range(n):
            am[i, j] = A[i, j]
    
    for i in range(n):
        am[i, n+i] = 1

    for i in range(n):
        for j in range(i + 1, n):
            lam = am[j, i] / am[i, i]
            am[j] -= lam * am[i]

    sm = np.zeros((n, n))

    for i in range(n - 1, -1, -1):
        for j in range(n):
            sm[i, j] = am[i, n+j]
            for k in range(i + 1, n):
                sm[i, j] -= am[i, k] * sm[k, j]

            sm[i, j] /= am[i, i]

    return sm



print('Inverse Matrix')
y = gi()
print(y)
