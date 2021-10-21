def solution(n, lost, reserve):
    answer = n-len(lost)
    lost.sort()
    reserve.sort()
    for i in lost:
        print(i)
        if i in reserve:
            reserve.remove(i)
            answer += 1
            continue
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
            continue
        elif i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
            continue
    return answer

print(solution(5, [3, 5], [2, 4]))