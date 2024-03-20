from numpy import ones
import matplotlib.pyplot as plt


filename = input('Enter file name of the data points: ')

X = []
Y = []




def avg(lst):
    sum=0
    for i in lst:
        sum=i+sum
        average=sum/len(lst)
    return average
def B(X,Y):
    num=0
    den=0
    for i in range(0,len(X)):
        num=(Y[i]*(X[i]-avg(X)))+num
    for i in range(0,len(X)):
        den=(X[i]*(X[i]-avg(X)))+den
    b=num/den
    return b         
def A (b):
    ans=(-1*b*avg(X))+avg(Y)
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

