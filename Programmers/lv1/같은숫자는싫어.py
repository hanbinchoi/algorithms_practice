def solution(arr):
    answer = []
    cursor = -9999
    for i in arr:
        if cursor != i:
            cursor = i
            answer.append(cursor)

    return answer

print(solution([1,1,3,3,0,1,1]))