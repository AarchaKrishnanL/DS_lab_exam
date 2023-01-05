import numpy as np
X=[2,5],[3,7]
Y=[5,1],[8,2]
Z=[1,4],[3,1]
print('Matrix X:',X)
print('Matrix Y:',Y)
print('Matrix Z:',Z)
a=np.multiply(X,X)
b=np.multiply(2,Y)
ca=np.multiply(Z,Z)
c=np.multiply(ca,Z)
d=np.add(a,b)
e=np.subtract(d,c)
print('X^2+2Y-Z^3 :')
print(e)