def solution(scoville, K):
    scoville.sort()
    cnt = 0
    while min(scoville)<K:
        a = scoville.pop(0)
        cnt += 1
        if len(scoville) != 1:
            b = scoville.pop(0)
            new = a+(b*2)
        else:
            new = a + (a*2)
        scoville.append(new)
        scoville.sort()
        print(scoville)
    return cnt


print(solution([1, 2, 3, 9, 10, 12], 100))