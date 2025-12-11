freshRange = {}
freshList = []
amountFresh = 0

file = open('AoC 2025\Day 5\Input.txt', 'r') #creates a dictionary of fresh ranges and a list of the begining of the range to be sorted
for line in file:
    number = line.strip()
    if number.count('-') == 1:
        split = number.split('-')
        if freshList.count(int(split[0])) == 0: #checks if a key already exists in the dictionary and keeps the highest value or adds the new range
            freshList.append(int(split[0]))
            freshRange[int(split[0])] = int(split[1])
        elif int(split[1]) > freshRange[int(split[0])]:
            freshRange[int(split[0])] = int(split[1])
file.close()
freshList.sort() #sorts the keys so only neighboring ranges need to be checked for overlap

print('checking overlaps,', len(freshList), 'individual ranges found') #iterates through every range and checks if it overlaps with the range before it
for x in range(1, len(freshList)):
    if freshRange[freshList[x-1]] >= freshList[x]: 
        if freshRange[freshList[x]] > freshRange[freshList[x-1]]: #replaces the value of the lowest overlapping key with the highest value
            freshRange[freshList[x-1]] = freshRange[freshList[x]]
        freshList.pop(x)
        freshList.insert(x, freshList[x-1]) #replaces the higher overlapping key with the lower so the updated range can be compared in the next loop 
freshList = list(set(freshList)) # removes duplicates

print('overlaps merged', len(freshList), 'individual ranges remaining')
for x in freshList:
    amountFresh += freshRange[x] - x + 1 # adds the amount of numbers in all the ranges together
print(amountFresh, 'ingredients are fresh')