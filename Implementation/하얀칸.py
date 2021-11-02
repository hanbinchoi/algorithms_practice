maps = []
answer = 0
for i in range(8):
    maps.append(input())

for i in range(0,len(maps),2):
    for j in range(0,len(maps[i]),2):
        if maps[i][j] == 'F':
            answer += 1
for i in range(1,len(maps),2):
    for j in range(1,len(maps[i]),2):
        if maps[i][j] == 'F':
            answer += 1
print(answer)