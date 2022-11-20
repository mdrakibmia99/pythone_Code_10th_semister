

# myArray=[10,30,5,3,0,20]

getArray = input("Enter array value:").split()
myArray = [int(intValue) for intValue in getArray]


def findMinValue(array):
    tempMin = array[0]
    for i in range(1, len(array)):
        if (tempMin > array[i]):
            tempMin = array[i]
    return tempMin


for i in range(0, len(myArray)-1):
    minValue = findMinValue(myArray[i:])
    valueIndex = myArray.index(minValue)
    myArray[i], myArray[valueIndex] = myArray[valueIndex], myArray[i]

print(myArray)
