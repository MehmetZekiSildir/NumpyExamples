import numpy as np

a=np.array([2,6,9,4,3,1,7,8,5])
print(a)
b=np.sort(a)
print(b)

c=np.random.normal(20,5,(3,3))
print(c)
d=np.sort(c,axis=0)
e=np.sort(c,axis=1)
print(d)
print(e)