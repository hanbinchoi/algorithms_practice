def solution(price, money, count):
    answer = -1
    priceSum = 0
    for i in range(1,count+1):
        priceSum += price*i

    if priceSum > money:
        return abs(money-priceSum)
    else:
        return 0
    return answer

print(solution(3,20,4))