def solution(ls):
    return min(len(ls)/2, len(set(ls)))
print(solution([3,1,2,3]))