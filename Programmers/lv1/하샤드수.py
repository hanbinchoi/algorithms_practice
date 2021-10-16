def solution(x):
    answer = True
    hasad = sum(list(int(x) for x in str(x)))
    if x%hasad == 0:
        return True
    return False

print(solution(10))