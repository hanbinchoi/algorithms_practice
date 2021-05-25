n,m,k = list(map(int, input().split()))

data = list(map(int,input().split()))
answer = 0
count = 0
first = True

data.sort()
while(True):
    if(first):
        for i in range(k):
            answer += data[n-1]
            count += 1
            if (count == m): break
        first = False
    else:
        answer += data[n-2]
        count += 1
        if (count == m): break
        first = True

    if(count == m): break

print(answer)