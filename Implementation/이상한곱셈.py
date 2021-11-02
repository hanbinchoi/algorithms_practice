a,b = input().split()

aNums = [int(i) for i in a]
bNums = [int(i) for i in b]
ans = 0
ans = sum(aNums)*sum(bNums)
print(ans)

