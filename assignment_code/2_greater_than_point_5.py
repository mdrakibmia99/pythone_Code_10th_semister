
#find the value in the matrix of which are grater-than 0.5
import numpy as np

matrixArray=np.random.random((3,3))
print('3x3 Matrix with random number:\n',matrixArray)
largestValue=matrixArray[matrixArray > 0.5]
print("\n\nThe Values of matrix Grater-than 0.5:\n",largestValue)