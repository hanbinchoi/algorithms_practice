import math
from itertools import permutations


def is_prime_number(n):
    """소수판별 함수"""
    if n == 0 or n == 1:  # 0,1 은 소수가 아님
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):  # sqrt(n)까지만 for문을 돌면서 확인하면 된다.
            if n % i == 0:  # 2~sqrt(num)까지 나누어 떨어지는 숫자가 있으면 소수가 아님
                return False

        return True

def solution(numbers):
    answer = set()
    for i in range(1, len(numbers)+1):
        arr = list(permutations(numbers,i))

        for j in arr:
            num = int(''.join(list(j)))
            print(num)
            if is_prime_number(num):
                answer.add(num)
    return len(answer)

print(solution("011"))

# permutation -> 순열 생성 -> 3개로 설정하면 3개 뽑아서 나올 모든 경우의 수 리턴
# combination -> 조합 -> 2개로 설정하면 2개 뽑아서 나오는 조합, 중복x (1,2), (2,1) 같은