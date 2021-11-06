def solution(ings, menu, sell):
    answer = 0
    priceDict = {}
    for i in ings:
        price = i.split()
        priceDict[price[0]] = int(price[1])
    moneyDict = {}
    for i in menu:
        item = i.split()
        foodDict = {}
        for j in priceDict.keys():
            if item[1].count(j):
                foodDict[j] = item[1].count(j)
        totalM = 0
        for key,value in foodDict.items():
            totalM += (priceDict[key])*int(value)

        moneyDict[item[0]] = int(item[2])- totalM

    for i in sell:
        item = i.split()
        answer += moneyDict[item[0]] * int(item[1])
    return answer

print(solution(["r 10", "a 23", "t 124", "k 9"],
               ["PIZZA arraak 145"],
               ["PIZZA 8"]))