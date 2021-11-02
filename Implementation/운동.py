N,m,M,T,R = map(int,input().split())

now = m
cnt = 0
ans = 0
while cnt!=N:
    next = now
    if now+T <= M:
        now += T
        cnt += 1
        ans += 1
    else:
        if now-R < m:
            now = m
        else:
            now -= R
        ans +=1
    if next == now:
        ans = -1
        break
print(ans)