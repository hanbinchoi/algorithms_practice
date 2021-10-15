def solution(d, budget):
    answer = 0
    d.sort()
    while budget > 0:
        budget -= d[0]
        d.pop(0)
        if budget >= 0:
            answer += 1
        else:
            break
        if len(d) == 0:
            break
    return answer

print(solution([1,3,2,5,4],	9))