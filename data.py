import csv

with open('data.txt', newline='') as input:
    results = list(csv.reader(input))[1:]
    current_player = ""
    repeats = []
    for player in results:
        if current_player != player[1]:
            current_player = player[1]
        else:
            repeats.append(player)
    for player in repeats:
        results.remove(player)

def getData():
    data = []
    for player in results:
        player = player[8:]
        three_point = player[5]
        two_point = player[8]
        free_throw = player[12]
        player.remove(three_point)
        player.remove(two_point)
        player.remove(free_throw)
        player = [float(i) for i in player]
        data.append(player)
    return data

def getPositions():
    positions = []
    for player in results:
        positions.append(player[2])
    return positions
# 
# print(getData()[14])
# print(getPositions()[14])
