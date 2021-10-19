def count(arr):
    one = 0
    zero = 0
    for i in arr:
        one += i.count(1)
        zero += i.count(0)
    return zero, one

def solution(arr):
    answer = []
    one = 0
    zero = 0
    print(count(arr))
    if count(arr)[0] == 0:
        one += 1
    elif count(arr)[1] == 0:
        zero += 1
    else:

    return [one,zero]

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))