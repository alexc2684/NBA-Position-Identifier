import csv

def getData():
    with open('data.txt', newline='') as input:
        data = list(csv.reader(input))
    return data

def getPositions():
    return [PF, SF, C, PG, SG]

#player = data[i]
#position = player[2]
