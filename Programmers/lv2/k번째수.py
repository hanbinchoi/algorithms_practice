def solution(array, commands):
    answer = []
    for i in commands:
        a = array[i[0]-1:i[1]]
        a.sort()
        answer.append(a[i[2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))