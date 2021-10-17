def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i,j in zip(A,B):
        answer += i*j
    return answer

print(solution([1, 4, 2],[5, 4, 4]))