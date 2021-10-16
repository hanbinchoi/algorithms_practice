def solution(strings, n):
    answer = []
    strings.sort(key=lambda x:(x[n],x))
    return strings

print(solution(["sun", "bed", "car"],1))