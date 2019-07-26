#test run
import csv

#creating a file for testing
#createdfile file
with open('createdFile.csv', mode = 'w') as createdFile:
    createdWriter = csv.writer(createdFile, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
    createdWriter.writerow(['Test', 'Me'])
    

#First run Getting an array populated
placeHolder = 0
myArray = []
for i in range(0, 20):
    myArray.append(placeHolder)
    placeHolder += 1

print(myArray)

#A simple pseudo-random shakeup of an array's values
#It's a linear growth
import random

linearArray = []
for i in myArray:
    linearArray.append(myArray[i] + 0.1 * random.randint(0,50))
    
print(linearArray)

#A string's iterations
myString = "Item "
placeHolder = 1;

itemArray = []

for i in range(0,20):
    itemArray.append(myString + str(placeHolder))
    placeHolder += 1
    
print(itemArray)

#Creates a string and a number to associate with that string
#Test 2 file
with open('test2.csv', mode = 'w') as test2File:
    createdWriter = csv.writer(test2File, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,20):
        createdWriter.writerow([itemArray[i], linearArray[i]])
        

#Making a non-linear sorting of random numbers, to 2 decimal places
#Specifically, a sine function
import math
import numpy as np

sinArray = []
for i in myArray:
    #this is to get a number to 2 places. Probably a better way exists
    sinArray.append("{0:.2f}".format(math.sin(myArray[i]) * 100))

    
    #This changes the array of string to array of float
sinArray = np.asarray(sinArray)
sinArray = sinArray.astype(np.float)
print(sinArray)


#First graph
import matplotlib.pyplot as plt

#graph of a linear correlation
plt.xlabel('Time')
plt.ylabel('Value')
plt.plot(myArray, linearArray, color='red')

#Scatter plot of a linear correlation
plt.xlabel('Time')
plt.ylabel('Value')
plt.scatter(myArray, linearArray, color='red')


#plotting a sine-like bit of data

plt.xlabel('Time')
plt.ylabel('Value')
plt.ylim(min(sinArray), max(sinArray))
plt.plot(myArray, sinArray)
print(myArray)
print(sinArray)
type(sinArray)


#A truly random Array of values

randomArray = []

for i in myArray:
    randomArray.append(myArray[i] + random.randint(0,50))
    
plt.xlabel('Time')
plt.ylabel('Value')
plt.ylim(min(randomArray), max(randomArray))
plt.plot(myArray, randomArray)
print(myArray)
print(randomArray)


#This is a little more defined. I'll be making a function here, eventually. Or based on this.
#It makes a simple, sample history of inventory. I can add fields, like names and such, easily when needed.

minItemsSoldPerDay = 0
maxItemsSoldPerDay = 20

numberOfDays = 60
numberInStock = 100

restockTime = 7
restockAmount = 100;

dayArray = []
randomArray = []
for i in range (0, numberOfDays + 1):
    dayArray.append(i)

#Intial Value
randomArray.append(numberInStock)
print("Starting number in stock is", numberInStock)

placeholder = 0;

#You have a # of items in stock. (user defined)
#This takes away a certain number per day (user defined)
#Then it adds the restock amount every x days (user defined) 
for i in range(0, numberOfDays):
    if placeholder == restockTime:
        numberInStock += restockAmount
        placeholder = 0
        print("Restock! Added", restockAmount)
        x = random.randint(0, maxItemsSoldPerDay)
        numberInStock -= x
        if numberInStock < 0:
            numberInStock = 0
        print("Number removed is:", x, "number in stock is now", numberInStock)
        randomArray.append(numberInStock)
    else:
        x = random.randint(0, maxItemsSoldPerDay)
        numberInStock -= x
        if numberInStock < 0:
            numberInStock = 0
        print("Number removed is:", x, "number in stock is now", numberInStock)
        randomArray.append(numberInStock)
        placeholder += 1


print("Stock over the", numberOfDays, "days:", randomArray)

plt.xlabel('Time')
plt.ylabel('Value')
plt.ylim(min(randomArray), max(randomArray))
plt.plot(dayArray, randomArray)


#Saving the previous thing to a csv
#sample file
dayArray = []
placeHolder = 0;
myString = "Day number "

for i in range(0,numberOfDays+ 1):
    dayArray.append(myString + str(placeHolder))
    placeHolder += 1
    
with open('sample.csv', mode = 'w') as sampleFile:
    myWriter = csv.writer(sampleFile, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,numberOfDays+ 1):
        #myWriter.writerow(['Test', 'Me'])
        myWriter.writerow([dayArray[i], randomArray[i]])