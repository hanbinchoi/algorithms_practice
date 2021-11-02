def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        print(citations[i],l-i )
        if citations[i] >= l-i:
            return l-i
    return 0
print(solution([20,19,1,3,5,6]))

# 작은 순서대로 소팅 -> 현재 논문이 인용된 수가 나머지 논문 중 현재 논문만큼 인용된 수보다 크다