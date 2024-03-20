from numpy import abs
x=float(input('enter root estimation: '))
def f(x):
    y=((x**2)-(3*x)+3)**(-1)
    return y
def fd(x):
    h=0.0001
    dydx=(4*f(x+h)-f(x+2*h)-3*f(x))/(2*h)
    return dydx
def NR(x):
    dx=2*x
    while abs(f(x)-x)>0.0001:
        dx=(-1*(f(x)/fd(x)))
        x=x-dx
    return x
print(NR(x))
print(f(1))
