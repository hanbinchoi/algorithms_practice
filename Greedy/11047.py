n, k = map(int,input().split())

units = []
for i in range(n):
    units.append(int(input()))

units.sort(reverse=True)
ans = 0
while k!=0:
    ans += k//units[0]
    k = k%units.pop(0)

print(ans)