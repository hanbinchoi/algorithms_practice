def solution(num):
    answer = num
    cnt = 0
    while True:
        if cnt == 500:
            return -1
        if answer==1:
            break
        if answer%2 == 0:
            answer = answer//2
        else:
            answer = answer*3 + 1
        cnt += 1
        if answer==1:
            break

    return cnt

print(solution(1))