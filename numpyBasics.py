import numpy as np
print(np.__version__)



NumpyList  = np.ones((3,3))
print(NumpyList)

NumpyList = np.pad(NumpyList, pad_width = 1, mode='constant', constant_values=0)

print(NumpyList)