freshRange = []
ingredientID = []
amountFresh = 0

file = open('AoC 2025\Day 5\Input.txt', 'r') #creates a list of fresh ranges and a list of IDs
for line in file:
    number = line.strip()
    if number.isdigit():
        ingredientID.append(int(number))
    elif number.count('-') == 1:
        freshRange.append(number)
file.close()

def isFresh(IDnum): #iterates through list of ranges and checks if ID is inbetween any of them
    for x in freshRange:
        split = x.split("-")
        if IDnum >= int(split[0]) and IDnum <= int(split[1]):
            print(x)
            return(True)
    return(False)

for x in ingredientID: #iterates through list of IDs
    print('checking ID', x)
    if isFresh(x):
        print('fresh')
        amountFresh += 1
    else:
        print('spoiled')
print(amountFresh, 'ingredients are fresh')