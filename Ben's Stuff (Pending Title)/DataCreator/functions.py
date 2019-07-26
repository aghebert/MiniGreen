import random
import matplotlib.pyplot as plt
import csv


def fileCreation(number):
    print("test", number)
    print(type(number))
    
fileCreation(20)


#Creates a simple array
def createSimpleArray(arraySize):
    placeHolder = 0
    myArray = []
    for i in range(arraySize):
        myArray.append(placeHolder)
        placeHolder += 1
    return myArray

simpleArray = createSimpleArray(20)
print(simpleArray)


#populates an array of x size, x being the array placed in
def randomArray(internalArray):
    randomArray = []

    for i in internalArray:
        randomArray.append(internalArray[i] + random.randint(0,50))
    return randomArray

randomArray = randomArray(simpleArray)
print(randomArray)



def sample1(minItemsSoldPerDay, maxItemsSoldPerDay,numberOfDays,
numberInStock, restockTime, restockAmount):
    
    valueArray = []
    
    placeholder = 0;
    for i in range(0, numberOfDays):
        if placeholder == restockTime:
            numberInStock += restockAmount
            placeholder = 0
            #print("Restock! Added", restockAmount)
            x = random.randint(0, maxItemsSoldPerDay)
            numberInStock -= x
            if numberInStock < 0:
                numberInStock = 0
            #print("Number removed is:", x, "number in stock is now", numberInStock)
            valueArray.append(numberInStock)
        else:
            x = random.randint(0, maxItemsSoldPerDay)
            numberInStock -= x
            if numberInStock < 0:
                numberInStock = 0
            #print("Number removed is:", x, "number in stock is now", numberInStock)
            valueArray.append(numberInStock)
            placeholder += 1
    return valueArray
    
myStuff = sample1(0, 20, 60, 100, 7, 80)
print(myStuff)

def dayMaker(myStuff):
    dayArray = []
    placeholder = 0
    for i in range(0, len(myStuff)):
        dayArray.append(placeholder)
        placeholder+=1
    return dayArray

days = dayMaker(myStuff)
print(days)

def printMe(valueArray, dayArray):
    plt.xlabel('Time')
    plt.ylabel('Number')
    plt.ylim(min(valueArray), max(valueArray))
    plt.plot(dayArray, valueArray)

printMe(myStuff, days)


def fileCreator(name, dayArray, valueArray):
    with open(name + '.csv', mode = 'w') as sampleFile:
        myWriter = csv.writer(sampleFile, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, len(dayArray)):
            #myWriter.writerow(['Test', 'Me'])
            myWriter.writerow([dayArray[i], valueArray[i]])
            
fileCreator("TestingThis", days, myStuff)