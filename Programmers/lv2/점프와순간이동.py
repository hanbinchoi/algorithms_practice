def solution(n):
    k = 1
    while k<n:
        k *= 2
    n=k//2
    k=1
    return n-(k//2)+1

print(solution(5000))