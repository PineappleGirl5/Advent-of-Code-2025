import re

grandTotal = 0
file = open('AoC 2025\Day 6\Input.txt', 'r') #creates a list with each line in the file
tempList = []
for line in file:
    tempList.append(line)
file.close()
firstNumList = tempList[0]
secondNumList = tempList[1]
thirdNumList = tempList[2]
fourthNumList = tempList[3]
operatorList = tempList[4]

for x in range(0, len(operatorList)-1): 
    if not operatorList[x].isspace(): #detects the next set of numbers by finding the first coloumn with an operator symbol
        currentNums = []
        for i in range(0, 4):
            if x+i <= len(firstNumList)-1: #reformats the numbers into the correct order in a list
                grabNum = firstNumList[x+i] + secondNumList[x+i] + thirdNumList[x+i] + fourthNumList[x+i]
                if grabNum.isspace():
                    break
                grabNum = grabNum.strip()
                currentNums.append(int(grabNum))
        currentNums.reverse()
        print(currentNums)
        addon = currentNums[0]
        for i in range(1, len(currentNums)): #adds or multiplies the numbers together and adds them to the total
            if operatorList[x] == '*':
                addon = addon * currentNums[i]
            else:
                addon = addon + currentNums[i]
        grandTotal += addon
print(grandTotal)