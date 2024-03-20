def f(a):
    y=a**2
    return y
def forwardderiv(x,h):
    dydx=(4*f(x+h)-f(x+2*h)-3*f(x))/(2*h)
    return dydx
def backwardderiv(x,h):
    dydx=(f(x-2*h)+3*f(x)-4*f(x-h))/(2*h)
    return dydx
def centralderive(x,h):
    dydx=(f(x+h)-f(x-h))/(2*h)
    return dydx
def forwarddderiv(x,h):
    dydx=(f(x)-2*f(x+h)+f(x+2*h))/(h**2)
    return dydx
def centraldderiv(x,h):
    dydx=(f(x-h)-2*f(x)+f(x+h))/(h**2)
    return dydx
x=float(input('enter value of x to differentiate: '))
h=float(input('enter value of h: '))
print('the derivative at the given point is: ',forwardderiv(x,h))




