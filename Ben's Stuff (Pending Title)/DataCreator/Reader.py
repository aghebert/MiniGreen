import csv

with open('TestingThis.csv', 'r', newline = "\n") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)