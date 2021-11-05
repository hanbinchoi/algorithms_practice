from itertools import combinations

def is_prime(num):
    if num == 0 or num == 1:
        return False
    cnt = 0
    for i in range(2,num+1):
        if num%i == 0:
            cnt +=1
        if cnt == 2:
            return False
    return True
def solution(nums):
    answer = 0
    numThree = list(combinations(nums,3))
    for i in numThree:
        if is_prime(sum(i)): answer +=1


    return answer

print(solution([1,2,3,4]))