#4_Create a 4x4 matrix B with random values find it transpose
import numpy as np
B=np.random.randint(100,size=(4,4))
transposeMatrix=B.transpose()
print("\nBefore Transpose matrix\n",B)
print("\nAfter Transpose Matrix\n",transposeMatrix)