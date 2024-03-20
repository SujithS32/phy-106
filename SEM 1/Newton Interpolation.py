from numpy import*

X=array([-2,1,4,-1,3,-4],float)
Y=array([-1,2,59,4,24,-53],float)
n=6
x=2
a=Y.copy()

for i in range(1,n):
    for j in range(i,n):
        a[j]=(a[j]-a[i-1])/(X[j]-X[i-1])
p=a[n-1]
for i in range(2,n+1):
    p=a[n-i]+(x-X[n-i])*p
print('y(x)=',p)
