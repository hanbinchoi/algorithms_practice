def solution(a, b):
    answer = [x for x in range(min(a,b),max(a+1,b+1))]
    return sum(answer)

print(solution(3,5))