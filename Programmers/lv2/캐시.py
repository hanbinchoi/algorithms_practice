def solution(cacheSize, cities):
    answer = 0
    cacheList = []
    for i in cities:
        if cacheSize == 0:
            return len(cities)*5
        i = i.upper()
        if i in cacheList:
            index = cacheList.index(i)
            cacheList.pop(index)
            cacheList.append(i)
            answer += 1
        else:
            if len(cacheList) < cacheSize:
                cacheList.append(i)
            else:
                cacheList.pop(0)
                cacheList.append(i)
            answer += 5
        print(cacheList)
    return answer

print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))