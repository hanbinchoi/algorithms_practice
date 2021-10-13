def solution(nums):
    answer = 0
    choice = nums//2
    if choice>= len(set(nums)):
        answer = choice
    else:
        answer = len(set(nums))
    return answer

print(solution([3,3,3,2,2,4]))