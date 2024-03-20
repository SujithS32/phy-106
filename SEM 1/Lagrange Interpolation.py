from numpy import *

def lagrange_interpolate(X, Y, n, x):
    p = 0.0
    for i in range(n):
        term = Y[i]
        for j in range(n):
            if i != j:
                term = term * ((x - X[j]) / (X[i] - X[j]))
        p = p + term
    return p

n = int(input('Enter number of data points: '))
x = float(input('Enter the x value for interpolation: '))

Y = [4,6,8,9]
X = [-2,1,2,5]



result = lagrange_interpolate(X, Y, n, x)
print('Interpolated value at x =', x, 'is y =', result)