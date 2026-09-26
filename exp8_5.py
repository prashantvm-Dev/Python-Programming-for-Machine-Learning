import numpy as np
x=np.array([1,2,3,4])
np.save('myarr',x)
loadarr=np.load('myarr.npy')
print("Loaded array:",loadarr)