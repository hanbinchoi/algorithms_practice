n = input()
n =n.upper()

nDict = {}

for i in n:
    if nDict.get(i):
        nDict[i] += 1
    else:
        nDict[i] = 1
val = max(nDict.values())
valC = ''
cnt = 0
for i in nDict:
    if nDict[i] == val:
        valC = i
        cnt += 1
    if cnt > 1:
        valC = '?'
        break
print(valC)