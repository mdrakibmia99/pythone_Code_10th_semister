import pandas as pd
import numpy  as np

fullTable = pd.read_csv('likelyHoodMatrix.csv')
def likelyHoodFunction(uniqueSpeciesValueLen,select):
    matrixArray = []
    uniqueHeaderValue = fullTable[select].unique()
    uniqueHeaderValueLen=len(uniqueHeaderValue)
    for i in range(0, uniqueHeaderValueLen):
        for j in range(0, uniqueSpeciesValueLen):
            CSh = ((fullTable[select] == uniqueHeaderValue[i]) & (fullTable.species == uniqueSpeciesValue[j])).sum()
            speciesTotalValue = (fullTable.species == uniqueSpeciesValue[j]).sum()
            matrixArray.append(CSh / speciesTotalValue)
    print(select," and species matrix wil be :", uniqueHeaderValueLen, "X", uniqueSpeciesValueLen, "matrix")
    print(uniqueHeaderValue, "select column direction")
    print(np.reshape(matrixArray, (uniqueHeaderValueLen, uniqueSpeciesValueLen)),"\n")

uniqueSpeciesValue = fullTable.species.unique()
uniqueSpeciesValueLen = len(uniqueSpeciesValue)
print(fullTable)
print(uniqueSpeciesValue,"this is target value\n")

# color and species matrix
likelyHoodFunction( uniqueSpeciesValueLen,"color")

# legs and species matrix
likelyHoodFunction( uniqueSpeciesValueLen,"legs")

# height and species matrix
likelyHoodFunction(uniqueSpeciesValueLen,"height")

# smelly and species matrix
likelyHoodFunction(uniqueSpeciesValueLen,"smelly")


