from numpy import*

X = array([[4, -2, 1],
           [-2, 4, -2],
           [1, -2, 4],], float)
Y = array([11, -16, 17], float)

n = 3


def UM(X, Y, n):
    for k in range(n-1):
        for i in range(k+1, n):
            lam = X[i, k] / X[k, k]
            for j in range(k, n): 
                X[i, j] = X[i, j] - lam * X[k, j]
            Y[i] = Y[i] - lam * Y[k]
    return X, Y

X,Y=UM(X,Y,n)

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



def gaussPivot(a, b, tol=1.0e-9):
    n = len(b)
    s = zeros(n, dtype=float)
    for i in range(n):
        s[i] = max(abs(a[i, :]))
    for k in range(n-1):
        p = argmax(abs(a[k:n, k]) / s[k:n]) + k
        if abs(a[p, k]) < tol:
            raise ValueError('Matrix is singular')  # Raise an error if matrix is singular
        if p != k:
            b[[k, p]] = b[[p, k]]
            a[[k, p]] = a[[p, k]]
            s[k], s[p] = s[p], s[k]
        for i in range(k+1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k+1:n] -= lam * a[k, k+1:n]
                b[i] -= lam * b[k]
    if abs(a[n-1, n-1]) < tol:
        raise ValueError('Matrix is singular')
    return a, b  # Gaussian elimination with pivoting

def backsub(X, Y, n):
    x = zeros(n, dtype=float)
    x[n-1] = Y[n-1] / X[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (Y[i] - dot(X[i, i+1:n], x[i+1:n])) / X[i, i]
    return x

X, Y = gaussPivot(X, Y)  # Perform Gaussian elimination with pivoting

print(X, Y)
result = backsub(X, Y, n)  # Perform back substitution
print('the result is:',result)

