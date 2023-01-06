import pandas as pd

fullTable = pd.read_csv('likelyHoodMatrix.csv')
print(fullTable)

# likelyHoodFunction create 
def likelyHoodFunction(inputArray,HeadingValueList,speciesValue):
    totalSpeciesValue=len(fullTable.species)
    uniqueSpecies = (fullTable.species== speciesValue).sum()
    probability=uniqueSpecies/totalSpeciesValue
    for i in range(len(inputArray)):
        countValue=((fullTable[HeadingValueList[i]] == inputArray[i]) & (fullTable.species == speciesValue)).sum()
        values=countValue/uniqueSpecies
        probability=probability * values
    return probability
        

# get all require input 
getColor=input("Enter Color Name:")
getLegs=int(input("Enter Legs Value:"))
getHeight=input("Enter height value:")
getSmelly=input("Enter smelly value:")     
# all input add in a array 
inputArray=[getColor,getLegs,getHeight,getSmelly]
# This is all heading value list in a array 
HeadingValueList=["color","legs","height","smelly"]
# Store value for species M 
storeProbabilityM = likelyHoodFunction(inputArray,HeadingValueList,'m')

# Store value for species H 
storeProbabilityH=likelyHoodFunction(inputArray,HeadingValueList,'h')

if(storeProbabilityM>storeProbabilityH):
    print('Species will be = m')
else:
    print('Species will be = h')

