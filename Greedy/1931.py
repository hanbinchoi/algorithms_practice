n = int(input())
meeting = []
for i in range(n):
    s,e = map(int,input().split())
    meeting.append([s,e,e-s])

meeting.sort(key=lambda x:x[1])
ans = 0
while meeting:
    k = meeting.pop(0)
    ans +=1
    meeting = [i for i in meeting if k[1]<=i[0]]
print(ans)