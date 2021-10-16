def solution(arr):
    answer = []
    arr.remove(min(arr))
    if len(arr) == 0:
        return [-1]
    return arr

print(solution([4,3,2,1]))