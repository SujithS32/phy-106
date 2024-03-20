from math import log10 as ln
from math import ceil
from numpy import abs
x1=float(input('enter the value of x1: '))
x2=float(input('enter the value of x2: '))
x3=0
ans=0

ep=float(input('enter the value of epsilon: '))

def f(x):
    y=(x**3) - 2 
    return y
def bisect(x1,x2,ep):
    c=0
    while abs(x2-x1)>=ep:
        c=c+1
        x3=(x1+x2)/2
        if f(x1)*f(x3)>0:
            x1=x3
        else:
            x2=x3
    ans=(x2+x1)/2
    print(c)
    return ans
print(bisect(x1,x2,ep))