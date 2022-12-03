# 2-dimensional matrix into one dimensional array
import numpy as np

matrixArray=np.random.random((3,3))

oneDimension=matrixArray.flatten()
print("\n2-dimensional array:\n",matrixArray) 
print("\n\nOne dimensional array:\n",oneDimension) 