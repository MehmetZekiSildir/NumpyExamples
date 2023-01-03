#6x+2y=15
#x+4y=10

import numpy as np

a=np.array([[6,2],[1,4]])
b=np.array([15,10])
sonuc=np.linalg.solve(a,b)
print(sonuc)