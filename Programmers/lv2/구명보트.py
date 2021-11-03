def solution(people, limit):
    answer = 0
    people.sort()

    cnt = 0
    i = 0
    j = len(people)-1
    while i <= j:
        cnt += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return cnt

print(solution([100,500,500,900,950 ], 1000))