import csv

with open('data.txt', newline='') as input:
    data = list(csv.reader(input))

def getData():
    return data

def getPositions():
    results = []
    for player in data:
        results.append(player[2])
    return results

# print(getData()[1])
# print(getPositions()[1])
