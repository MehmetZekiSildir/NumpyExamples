import numpy as np
a=np.arange(0,30,3)
print(a)
b=[a[0],a[3],a[6]]
print(b)
###########################
fancy=[0,3,6]
print(fancy)
print(a[fancy])
###########################
c=np.arange(9).reshape(3,3)
print(c)
satir=np.array([0,1])
sutun=np.array([1,2])
print(c[satir,sutun])
##########################
