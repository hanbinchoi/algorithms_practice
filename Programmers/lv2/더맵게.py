def solution(scoville, K):
    answer = 0
    scoville.sort();
    cnt = 0
    while scoville:
        if len(scoville) <= 1:
            cnt = -1
            break
        cnt += 1
        scovilleScore = scoville[0] + (scoville[1]*2)
        if scovilleScore >= K:
            break
        else:
            scoville.append(scovilleScore)
            scoville.pop(0)
            scoville.pop(0)
            scoville.sort()
    if len(scoville) == 0:
        cnt = -1
    return cnt

print(solution([1,2,3],11))