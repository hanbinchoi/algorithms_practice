def solution(clothes):
    answer = 0
    cDict = dict()
    for i in clothes:
        if i[1] in cDict: cDict[i[1]] += 1
        else: cDict[i[1]] = 1
    cnt = 1
    for i in cDict.values():
        cnt *= (i+1)

    return cnt-1

print(solution(	[["crow_mask", "face"], ["blue_sunglasses", "a"], ["smoky_makeup", "a"],["smoky_makeup", "b"]]))

# 경우의 수 문제: 모든 카운트 다 곱하는데 어떤 건 안 입는 경우가 있으니 +1, 마지막에 모두 안 입는 경우는 없다고 했으니 -1