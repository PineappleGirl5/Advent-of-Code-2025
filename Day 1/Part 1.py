Dailpos = 50 # starting postion of dial is 50
TimesZero = 0 # the number of times the dial stoped on zero will be the output

def TurnDial (direction, amount):
    global Dailpos
    global TimesZero
    if direction == 'R':
        Dailpos += amount
    else:
        Dailpos -= amount
    
    while Dailpos > 99:
        Dailpos -= 100
    while Dailpos < 0:
        Dailpos += 100

    if Dailpos == 0:
        TimesZero += 1  
    
    print ('turned dial ',direction,amount,'stoping on ',Dailpos)

file = open ('AoC 2025\Day 1\Input.txt', 'r')
for line in file:
    Instruction = line.strip()
    print (Instruction)
    TurnDial (Instruction[0], int(Instruction[1:]))
file.close()
print ('the dial landed on zero ',TimesZero,' times')