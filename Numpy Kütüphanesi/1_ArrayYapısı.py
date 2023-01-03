import numpy as np
#np.array=matris oluştururuz.
a=np.array([1,2,3,4,5])
print(a)
print(type(a))
#dtype="int" oluşturulan matrisin elemanlarını integer yapar.
b=np.array([3.14,6,11,18],dtype="int")
print(b)
#np.zeros 10 elemanlı sıfır matris oluşturur.
c=np.zeros(10,dtype="int")
print(c)
#np.ones 10 elemanlı birim matris oluşturur.
d=np.ones(10,dtype="int")
print(d)
#np.zeros 5*6 lık elemanlı birim matris oluşturur.
e=np.ones((5,6),dtype="int")
print(e)
#np.full 3*4 lük bütün elemanlanlar 6 olur.
f=np.full((3,4),6)
print(f)
#np.arrange 0 ile 52 arasında 5 er 5 er ilerleyerek elemanları seçer ve matris oluşturur.
g=np.arange(0,52,5)
print(g)
#0 ve 1 arasında 20 elemanlı bir matris oluşturur.
h=np.linspace(0,1,20)
print(h)
#random rastgele üretüm için normal ortalama ve standart sapma girmek için kullanılan metodlardır.10 ortalama 4 standart sapma.
i=np.random.normal(10,4,(5,5))
print(i)
#np.random.randint 0 ile 15 arasında rastgele seçilecek rakamlarla 4*4 lük matris oluşturulur.
j=np.random.randint(0,15,(4,4))