import math

n = int(input())
pense = list(map(int,input().split()))
pense.sort(reverse=True)
p=0
while len(pense)>=3:
    print(pense)
    if pense[0] >= pense[1] >= pense[2]:
        if pense[0]<pense[1]+pense[2]:
            p = (pense[0]+pense[1]+pense[2])/2
            break
        else:
            pense.pop(0)
    else:
        pense.pop(0)

ans = p*(p-pense[0])*(p-pense[1])*(p-pense[2])

print(math.sqrt(ans))