Output = 0

file = open('AoC 2025\Day 2\Input.txt', 'r') #creates a list of each set of ranges
Input = (file.read()).split(',')
file.close()

def FindInvalid(IDNum):
    global Output
    print('checking ID#', IDNum)
    IDstr = str(IDNum)
    numbers = dict()
    for x in IDstr:
        if x not in numbers.keys(): #creates a dictionary of each number in the ID and it's frequency
            numbers[x] = 1
        else:
            numbers[x] += 1
    print(numbers)

    LowestNum = numbers[IDstr[0]] #finds the lowest frequency of a number
    for x in numbers:
        if numbers[x] < LowestNum:
            LowestNum = numbers[x]
    
    if LowestNum == 1: #returns valid if there is only one of any number in the sequence
        print('valid')
        return
    elif LowestNum == len(IDstr): #returns invalid if the entire sequence is comprised of the same digit repeating
        print('invald')
        Output += IDNum
        return
    
    Pattern = []
    SplitSize = int(len(IDstr)/LowestNum) #splits the sequense into sections based off of the lowest frequency number
    print(SplitSize)
    for x in range(0, LowestNum):
        SplitSection = (SplitSize*x)
        Pattern.append(IDstr[SplitSection:(SplitSection+SplitSize)])
    print(Pattern)


for x in Input: #seperates the range into the high and low numbers and iterates through
    print('serching range', x)
    Range = x.split('-')
    Low = int(Range[0])
    High = int(Range[1])
    for x in range(Low, High+1):
        FindInvalid(x)

print('output is', Output)