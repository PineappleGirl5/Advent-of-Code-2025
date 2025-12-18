manifold = []
timesSplit = 0
file = open('AoC 2025\Day 7\Input.txt', 'r')
for line in file:
    manifold.append(line.strip())
file.close()

start = manifold[0].find('S')
manifold[1] = (manifold[1])[:start] + '|' + (manifold[1])[start+1:] #starts the beam
print(manifold[0])

for x in range(1, len(manifold)):
    for i in range(0, len(manifold[x])): #iterates through every line and either splits or continues the beam
        if (manifold[x-1])[i] == '|':
            if (manifold[x])[i] == '^':
                timesSplit += 1
                manifold[x] = (manifold[x])[:i-1] + '|' + (manifold[x])[i:i+1] + '|' + (manifold[x])[i+2:]
            else:
                manifold[x] = (manifold[x])[:i] + '|' + (manifold[x])[i+1:]
    print(manifold[x])

print('beam split', timesSplit, 'times')