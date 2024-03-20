from numpy import ones
import matplotlib.pyplot as plt


filename = input('Enter file name of the data points: ')

X = []
Y = []
w = []
add=0
fhand = open(filename, 'r')

for line in fhand:
    if not line.startswith('#'):
        line=line.rstrip()
        a = line.split()
        X.append(float(a[0]))
        Y.append(float(a[1]))
                 
 

def wavg(lst):
    for i in w:
        add=(i**2)+add
    sum=0
    for i in lst:
        sum=(i*(w[i]**2))+sum
        average=sum/add
    return average
def B(X,Y):
    num=0
    den=0
    for i in range(0,len(X)):
        num=((w[i]**2)*Y[i]*(X[i]-wavg(X)))+num
    for i in range(0,len(X)):
        den=((w[i]**2)*X[i]*(X[i]-wavg(X)))+den
    b=num/den
    return b         
def A (b):
    ans=(-1*b*wavg(X))+wavg(Y)
    return ans
y1=[]
b=B(X,Y)
a=A(b)
for i in X:
    y=(b*i)+a
    y1.append(y)
plt.plot(X,Y)
plt.plot(X,y1)
plt.show()