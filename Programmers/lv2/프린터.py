def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])


    while True:
        item = d.popleft()

        if d and item[0] < max(d)[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break

    return answer


print(solution([2, 1, 3, 2], 2))


# 값과 인덱스로 queue 만듬 -> 하나씩 빼면서 최대값이면 찾는 로케이션과 비교 아니면 다음거, 최대값아니면 다시 뒤로 붙여줌