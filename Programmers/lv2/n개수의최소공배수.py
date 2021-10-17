def gcd(x,y):
    while y:
        x,y = y, x%y
    return x

def lcm(x,y):
    return x*y//gcd(x,y)

def solution(arr):
    answer = 0

    if len(arr) == 1: return arr[0]

    else:
        answer = lcm(arr[0],arr[1])
        arr.pop(0)
        arr.pop(0)
        while arr:
            answer = lcm(answer,arr[0])
            arr.pop(0)

    return answer

print(solution([2,6,8,14]))