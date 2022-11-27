#5_ create a 4x4 matrix then convert it 2*8 matrix (horizontal or vertical)
import numpy as np
B=np.arange(10,26).reshape(4,4)
horizontalMatrix=B.reshape(2,8)
print("4x4 Matrix\n",B)
print("\n Horizontal 2x8 Matrix \n",horizontalMatrix)