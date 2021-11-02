a,b,c = map(int,input().split())

aDice = [i+1 for i in range(a)]
bDice = [i+1 for i in range(b)]
cDice = [i+1 for i in range(c)]


diceDict = dict()

for i in aDice:
    for j in bDice:
        for k in cDice:
            num = i+j+k
            if diceDict.get(num):
                diceDict[num] += 1
            else:
                diceDict[num] = 1

for key, value in diceDict.items():
    if value == max(diceDict.values()):
        print(key)
        break