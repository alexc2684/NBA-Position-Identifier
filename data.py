import csv

with open('data.txt', newline='') as input:
    data = list(csv.reader(input))

print(data[0])
