freshRange = []
ingredientID = []
amountFresh = 0

file = open('AoC 2025\Day 5\Input.txt', 'r') #creates a list of fresh ranges and a list of IDs
for line in file:
    number = line.strip()
    if number.isdigit():
        ingredientID.append(number)
    elif number.count('-') == 1:
        freshRange.append(number)
file.close()

def isFresh(IDnum):
    for x in freshRange:
        split = x.split("-")
        #print(split)
        if IDnum >= split[0] and IDnum <= split[1]:
            print(x)
            return(True)
    return(False)

for x in ingredientID:
    print('checking ID', x)
    if isFresh(x):
        print('fresh')
        amountFresh += 1
    else:
        print('spoiled')
print(amountFresh, 'ingredients are fresh')