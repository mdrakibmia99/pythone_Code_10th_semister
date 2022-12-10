import pandas as pd
import numpy  as np

fullTable = pd.read_csv('likelyHoodMatrix.csv')
print(fullTable)

def likelyHoodFunction(inputArray,HeadingValueList,speciesValue):
    totalSpeciesValue=len(fullTable.species)
    uniqueSpecies = (fullTable.species== speciesValue).sum()
    probability=uniqueSpecies/totalSpeciesValue
    for i in range(len(inputArray)):
        countValue=((fullTable[HeadingValueList[i]] == inputArray[i]) & (fullTable.species == speciesValue)).sum()
        values=countValue/uniqueSpecies
        probability=probability * values
    return probability
        
getColor=input("Enter Color Name:")
getLegs=int(input("Enter Legs Value:"))
getHeight=input("ENter height value:")
getSmelly=input("Enter smelly value:")     
HeadingValueList=["color","legs","height","smelly"]

inputArray=[getColor,getLegs,getHeight,getSmelly]
print(inputArray)
# for species M 
forM=likelyHoodFunction(inputArray,HeadingValueList,'m')

# for species H 
forH=likelyHoodFunction(inputArray,HeadingValueList,'h')

if(forM>forH):
    print('Species will be = m')
else:
    print('Species will be = h')

