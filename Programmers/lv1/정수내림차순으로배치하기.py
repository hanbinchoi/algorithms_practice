def solution(n):
    answer = 0
    numList = []
    while n !=0:
        numList.append(n%10)
        n //= 10
    numList.sort(reverse=True)
    strVal =""
    for i in numList:
        strVal += str(i)

    return int(strVal)

print(solution(118372))