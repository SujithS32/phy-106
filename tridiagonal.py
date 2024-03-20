from numpy import array

def tridiag_decomp(c, d, e):
    n = len(d)
    for k in range(1, n):
        lam = e[k-1] / d[k-1]
        d[k] -= lam * c[k-1]
        e[k-1] = lam
    return c, d, e

def tridiag_solve(c, d, e, b):
    n = len(d)
    x = [0] * n
    for k in range(1, n):
        b[k] -= e[k-1] * b[k-1]
    x[-1] = b[-1] / d[-1]
    for k in range(n-2, -1, -1):
        x[k] = (b[k] - c[k] * x[k+1]) / d[k]
    return x

c = array([-1, -1, -1])
d = array([2, 2, 2, 2])
e = array([-1, -1, -1])
b = array([1, 0, 0, 1])


solution = tridiag_solve(c, d, e, b)

print("Solution:", solution)



