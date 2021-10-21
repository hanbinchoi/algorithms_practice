n, k = map(int,input().split())
unitList = []
for i in range(n):
    unitList.append(int(input()))

unitList.sort(reverse=True)
answer = 0
for i in unitList:
    answer += k//i
    k = k%i

print(answer)