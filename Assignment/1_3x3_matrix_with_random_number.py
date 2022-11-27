import numpy as np
# Create a 3x3 Matrix with random number
matrixArray=np.random.random((3,3))
print('3x3 Matrix with random number:\n',matrixArray)

#find the value in the matrix of which are grater-than 0.5
largestValue=matrixArray[matrixArray > 0.5]
print("\n\nThe Values of matrix Grater-than 0.5:\n",largestValue)

# 2-dimensional matrix into one dimensional array
oneDimension=matrixArray.flatten()
print("\n\n2-dimensional array:\n",matrixArray) 
print("One dimensional array:\n",oneDimension) 