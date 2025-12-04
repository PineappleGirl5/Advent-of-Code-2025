totalOutput = 0

def FindMax(bank):
    global totalOutput
    highestNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lastNum = -1
    for i in reversed(range(12)):
        temp = -1
        for x in range (lastNum+1, len(bank)-i): #finds the highest number in the line excluding the final digits and the numbers before the privous higher numbers
            if int(bank[x]) > int(highestNum[i]):
                highestNum[i] = (bank[x])
                temp = x
        lastNum = temp
        #print(lastNum)
    output = highestNum[11]
    for x in reversed(range(11)):  #adds the numbers together with the final output
        output = output + highestNum[x]
    print(highestNum)
    print(output)
    totalOutput += int(output)

file = open ('AoC 2025\Day 3\Input.txt', 'r') #opens file and iterates through every line
for line in file:
    currentBank = line.strip()
    print('finding output of bank', currentBank)
    FindMax(currentBank)
file.close()
print('total output joltage is', totalOutput)