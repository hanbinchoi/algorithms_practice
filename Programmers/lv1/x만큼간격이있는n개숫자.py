def solution(x, n):
    answer = []
    addVal = x
    while n!=0:
        answer.append(x)
        x += addVal
        n -= 1
    return answer

print(solution(2,5))