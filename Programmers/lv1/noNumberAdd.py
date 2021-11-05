def solution(numbers):
    answer = 0
    freq = [1,2,3,4,5,6,7,8,9,0]
    for i in numbers:
        freq.remove(i)
    return sum(freq)

print(solution([1,2,3,4,6,7,8,0]))