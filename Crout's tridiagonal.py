def trig(c, d, e, b):
    n = len(d)
    
    for i in range(1, n):
        temp = e[i-1] / d[i-1]
        d[i] = d[i] - temp * c[i-1]
        b[i] = b[i] - temp * b[i-1]
    
    
    x = [0] * n
    x[-1] = b[-1] / d[-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - c[i] * x[i+1]) / d[i]
    
    return x


c = [-1, -1, -1]  
d = [2, 2, 2, 2]  
e = [-1, -1, -1]  
b = [1, 0, 0, 1]  
solution = trig(c, d, e, b)
print("Solution:", solution)