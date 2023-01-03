import numpy as np
a=np.random.randint(10,size=(5,5))
print(a)
alt_kume_a=a[0:3,0:2].copy() #copy komutu asıl matrisi korur alt matrislerde eleman değişikliği olur.
print(alt_kume_a)
alt_kume_a[0,0]=1234
print(alt_kume_a)
alt_kume_a[0,1]=4567
print(alt_kume_a)
print(a)