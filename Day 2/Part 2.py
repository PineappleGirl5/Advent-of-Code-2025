Output = 0

file = open('AoC 2025\Day 2\Input.txt', 'r') #creates a list of each set of ranges
Input = (file.read()).split(',')
file.close()

def IsInvalid(IDNum):
    print('checking ID#', IDNum)
    IDstr = str(IDNum)
    numbers = dict()
    for x in IDstr:
        if x not in numbers.keys(): #creates a dictionary of each number in the ID and it's frequency
            numbers[x] = 1
        else:
            numbers[x] += 1
    #print('frequency of numbers:', numbers)

    LowestNum = numbers[IDstr[0]] #finds the lowest frequency of a number
    for x in numbers:
        if numbers[x] < LowestNum:
            LowestNum = numbers[x]
    
    if LowestNum == 1: #returns valid if there is only one of any number in the sequence
        return(False)
    elif LowestNum == len(IDstr): #returns invalid if the entire sequence is comprised of the same digit repeating
        return(True)
    
    Pattern = []
    SplitSize = len(IDstr)//LowestNum #splits the sequense into sections based off of the lowest frequency number
    #print('spliting into sections', SplitSize, 'numerals long')
    for x in range(0, LowestNum):
        SplitSection = (SplitSize*x)
        Pattern.append(IDstr[SplitSection:(SplitSection+SplitSize)])
    print(Pattern)

    Match = True
    for x in range(1, len(Pattern)): #returns invalid if all sections of the pattern match
        if Pattern[x] != Pattern[x-1]:
            Match = False
    if Match:
        return(True)
    
    if (len(Pattern)%2 == 1): #returns valid if there are an odd number of pattern sections
        return(False)
    
    while (len(Pattern)>2 and len(Pattern)%2 == 0): #combines every 2 items in the list to check if the pattern repeats in larger sections
        Combo = []
        for x in range(1, len(Pattern), 2):
            Combo.append(Pattern[x-1]+Pattern[x])
        Pattern.clear()
        Pattern.extend(Combo)
        print(Pattern)
        Match = True
        for x in range(1, len(Pattern)): #returns invalid if all sections of the pattern match
            print(len(Pattern))
            print(Pattern[x])
            print(Pattern[x-1])
            if Pattern[x] != Pattern[x-1]:
                Match = False
        if Match:
            return(True)


for x in Input: #seperates the range into the high and low numbers and iterates through
    print('serching range', x)
    Range = x.split('-')
    Low = int(Range[0])
    High = int(Range[1])
    for x in range(Low, High+1):
        if IsInvalid(x):
            Output += x
            print('invalid')
        else:
            print('valid')

print('output is', Output)