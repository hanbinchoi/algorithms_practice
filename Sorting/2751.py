num = int(input())
numList = []
for i in range(num):
    numList.append(int(input()))


numList.sort()

for i in range(num):
    print(numList[i])