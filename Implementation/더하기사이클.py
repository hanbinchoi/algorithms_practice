num = int(input())
k = num
cnt = 0

while True:
    a, b = k // 10, k % 10
    k = b * 10 + (a + b)%10
    cnt += 1
    if k==num:
        break
print(cnt)