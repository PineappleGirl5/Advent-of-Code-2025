import re

grandTotal = 0
file = open('AoC 2025\Day 6\Input.txt', 'r') #creates a list with each line in the file
tempList = []
for line in file:
    tempList.append(line.strip())
file.close()
firstNumList = re.split(r'[ ]+',tempList[0]) #creates a list of each number for each row in the file and removes all whitespace
secondNumList = re.split(r'[ ]+',tempList[1])
thirdNumList = re.split(r'[ ]+',tempList[2])
fourthNumList = re.split(r'[ ]+',tempList[3])
operatorList = re.split(r'[ ]+',tempList[4])

for x in range(0, len(firstNumList)): #adds or multiplies the numbers together and adds them to the total
    if operatorList[x] == '+':
        grandTotal += (int(firstNumList[x]) + int(secondNumList[x]) + int(thirdNumList[x]) + int(fourthNumList[x]))
    else:
        grandTotal += (int(firstNumList[x]) * int(secondNumList[x]) * int(thirdNumList[x]) * int(fourthNumList[x]))
print(grandTotal)