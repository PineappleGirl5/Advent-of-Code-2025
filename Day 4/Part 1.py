totalRolls = 0
paperRows = []
file = open('AoC 2025\Day 4\Input.txt', 'r') #creates a list with each item being a different row in the file
for line in file:
    paperRows.append(line.strip())
file.close()

def isReachable(row, column):
    rollsNearby = 0
    searchArea = '...'
    searchStart = 0
    searchEnd = 0
    if column != 0:
         searchStart = column - 1 #checks to see if target roll is on the edge to avoid out of bound erros when checking adjacent rolls 
    else:
         searchStart = column

    if column != len(paperRows[row]):
         searchEnd = column + 2
    else:
         searchEnd = column + 1

    if row != 0:
        searchArea = (paperRows[row-1])[searchStart:searchEnd] #checks spaces adjacent to target roll and counts them excluding the target roll
        print('counting rolls', searchArea)
        rollsNearby += searchArea.count('@')
    
    searchArea = (paperRows[row])[searchStart:searchEnd]
    print('counting rolls', searchArea)
    rollsNearby += searchArea.count('@') - 1

    if row != len(paperRows)-1:
        searchArea = (paperRows[row+1])[searchStart:searchEnd]
        print('counting rolls', searchArea)
        rollsNearby += searchArea.count('@')
    
    if rollsNearby < 4: #checks if there are too many rolls to be reachable or not
        return(True)
    else:
        return(False)


for x in range(len(paperRows)): #iterates through each column in each row
    print('searching row', x, paperRows[x])
    for i in range(len(paperRows[x])):
        print('checking column', i)
        if (paperRows[x])[i] == '@': #checks if target space has a roll to be reachable or not
            if isReachable(x, i):
                totalRolls += 1
                print('reachable')
            else:
                print('unreachable')
        else:
            print('no paper')

print(totalRolls, "rolls are reachable")