import numpy as np
x=np.array([12,52,41,33,66,78,83,91])
a,b,c=np.split(x,[3,5])
print(a)
print(b)
print(c)


d=np.arange(16).reshape(4,4)
print(d)
bol=np.vsplit(d,[2])
print(bol)