import pandas as pd
import numpy  as np

fullTable = pd.read_csv('likelyHoodMatrix.csv')
def likelyHoodFunction(uniqueSpecisValueLen,select):
    matrixArray = []
    uniqueHeaderValue = fullTable[select].unique()
    uniqueHeaderValueLen=len(uniqueHeaderValue)
    for i in range(0, uniqueHeaderValueLen):
        for j in range(0, uniqueSpecisValueLen):
            CSh = ((fullTable[select] == uniqueHeaderValue[i]) & (fullTable.specis == uniqueSpecisValue[j])).sum()
            specisTotalValue = (fullTable.specis == uniqueSpecisValue[j]).sum()
            matrixArray.append(CSh / specisTotalValue)
    print(select," and specis matrix wil be :", uniqueHeaderValueLen, "X", uniqueSpecisValueLen, "matrix")
    print(uniqueHeaderValue, "select coloumn direction")
    print(np.reshape(matrixArray, (uniqueHeaderValueLen, uniqueSpecisValueLen)),"\n")

uniqueSpecisValue = fullTable.specis.unique()
uniqueSpecisValueLen = len(uniqueSpecisValue)
print(fullTable)
print(uniqueSpecisValue,"this is target value\n")

# color and specis matrix
likelyHoodFunction( uniqueSpecisValueLen,"color")

# legs and specis matrix
likelyHoodFunction( uniqueSpecisValueLen,"legs")

# height and specis matrix
likelyHoodFunction(uniqueSpecisValueLen,"height")

# smelly and specis matrix
likelyHoodFunction(uniqueSpecisValueLen,"smelly")


