totalOutput = 0

def FindMax(bank):
    global totalOutput
    bankStr = str(bank)
    highestNum = 0
    for x in range (len(currentBank)-1): #finds the highest number in the line excluding the final digit
        if int(bankStr[x]) > highestNum:
            highestNum = int(bankStr[x])
    secondNum = 0
    for x in range(bankStr.find(str(highestNum))+1, len(bankStr)): #finds the highest number in the line located after the previous highest number
        if int(bankStr[x]) > secondNum:
            secondNum = int(bankStr[x])
    highestNum = str(highestNum)
    secondNum = str(secondNum)
    output = int(highestNum + secondNum) #adds the numbers together with the final output
    print(output)
    totalOutput += output

file = open ('AoC 2025\Day 3\Input.txt', 'r') #opens file and iterates through every line
for line in file:
    currentBank = line.strip()
    print('finding output of bank', currentBank)
    FindMax(currentBank)
file.close()
print('total output joltage is', totalOutput)