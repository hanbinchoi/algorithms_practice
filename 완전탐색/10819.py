from itertools import permutations

n = int(input())

nums = []

for i in range(n):
    nums.append(int(input()))


arr= permutations(nums,n)
res = 0
for i in arr:
    ans = 0
    for j in range(len(i)-1):
        ans += abs(i[j]-i[j+1])
    if ans>res:
        res=ans

print(res)