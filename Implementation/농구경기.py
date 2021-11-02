n = int(input())
nDict = dict()
for i in range(n):
    name = input()
    first = name[0]
    if nDict.get(first):
        nDict[first] += 1
    else:
        nDict[first] = 1
answer = ""
for key,values in nDict.items():
    if values >= 5:
        answer += key

if answer == "":
    print("PREDAJA")
else:
    print(answer)