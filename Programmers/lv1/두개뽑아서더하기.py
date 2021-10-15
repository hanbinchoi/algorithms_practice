def solution(numbers):
    answer = []
    k=1
    for i in numbers:
        for j in numbers[k:]:
            answer.append(i+j)
        k+=1

    answer = list(set(answer))
    answer.sort()
    return answer

print(solution([2,1,3,4,1]))
