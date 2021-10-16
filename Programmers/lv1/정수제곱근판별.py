def solution(n):
    answer = 0
    cnt=0
    for i in range(1,n+1):
        if n == i*i:
            cnt = i
            return (cnt + 1) ** 2
    print(cnt)
    if cnt == 0:
        return -1


print(solution(1))