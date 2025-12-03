Output = 0

file = open('AoC 2025\Day 2\Input.txt', 'r') #creates a list of each set of ranges
Input = (file.read()).split(',')
file.close()

def FindInvalid(IDNum):
    global Output
    #print('checking ID#', IDNum)
    IDString = str(IDNum)
    SplitAt = int(len(str(IDNum))/2)
    First = (IDString[:(SplitAt)])
    Second = (IDString[(SplitAt):])
    #print(First)
    #print(Second)
    if First == Second:
        Output += IDNum
        #print('invalid')
    #else:
        #print('valid')

for x in Input:
    print('serching range', x)
    Range = x.split('-')
    Low = int(Range[0])
    High = int(Range[1])
    for x in range(Low, High+1):
        FindInvalid(x)

print('output is', Output)