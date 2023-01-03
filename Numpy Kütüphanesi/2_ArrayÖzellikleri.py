# ndim:boyut sayisini belirtir.
# shape:boyut bilgisi
# size:toplam eleman sayısı
# dtype:array veri tipi


import numpy as np

a=np.random.randint(15,size=10)
print(a)
print(a.ndim)
print(a.size)
print(a.shape)
print(a.dtype)

b=np.random.randint(0,15,(5,5))
print(b)
print(b.ndim)
print(b.size)
print(b.shape)
print(b.dtype)