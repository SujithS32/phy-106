from math import *
lb=float(input('enter lower bound: '))
ub=float(input('enter upper bound: '))
c=float(input('enter order of accuracy: '))
dx=float(input('enter value of dx: '))
def f(x):
    y=pow(x,3)-10*pow(x,2)+5
    return y
x=0.0
f1=0.0
y=0.0
f2=0.0
def root_bracket(a,b,dx):
    x1=a
    f1=f(a)
    x2=a+dx
    f2=f(x2)
    while f1*f2>0.0:
     if x1>=b:
        return None,None
     x1=x2
     f1=f2
     x2=x1+dx
     f2=f(x2)
    else:
         return x1,x2

x,y=root_bracket(lb,ub,(ub-lb)/10**c)
root=((x+y)/2) 
print("Root is:",root)         
