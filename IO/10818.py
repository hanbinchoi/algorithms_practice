num = int(input())
numList = [int(x) for x in input().split()]
for i in range(num):
    if i==0:
        max = numList[i]
        min = numList[i]

    else:
        if(max<numList[i]): max=numList[i]
        if(min>numList[i]): min=numList[i]

print(min,max)