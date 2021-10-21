n = int(input())
meeting = []
for i in range(n):
    start,end = map(int,input().split())
    meeting.append([start,end])

meeting.sort(key=lambda x:(x[1],x[0]))
answer = 1
end = meeting[0][1]
meeting.pop(0)
for i in meeting:
    if end <= i[0]:
        end = i[1]
        answer += 1



print(answer)