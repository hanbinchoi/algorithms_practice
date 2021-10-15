def solution(numbers):
    answer = 0
    numFrequency = [0,1,2,3,4,5,6,7,8,9]
    for i in numFrequency:
        if not(i in numbers):
            answer += i
    return answer

print(solution([1,2,3,4,6,7,8,0]))