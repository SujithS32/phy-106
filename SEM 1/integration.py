from numpy import*
def f(x):
    y=(x**(1/2))
    return y
def Tintegral(a,b):
    h=b-a
    I=(h/2)*(f(a)+f(b))
    return I
def TCintegral(a, b, n):
    h = (b - a) / n
    x = arange(a, b +h , h)
    I = (f(a) + f(b))
    for i in range(1, n):
        I = I + (2 * f(x[i]))
    I = I * (h / 2)
    return I
def simpintegral(a,b):
    h=(b-a)/2
    I=(h/3)*(f(a)+4*(f(a+b)/2)+f(b))
    return I
def Csimpintegral(a,b,n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        integral += 4 * f(x[i])
    for i in range(2, n - 1, 2):
        integral += 2 * f(x[i])
    integral *= h / 3
    return integral
def simpintegralt(l):
    h=l[1]-l[0]
    sum=0
    for i in range(4):
        if i==3 or i==2:
            sum=l[i]*3+sum
        else:
            sum=l[i]+sum
    return (3*h/8)*sum
print(Tintegral(0,8))