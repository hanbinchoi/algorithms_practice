def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    for i in arr1:
        a = str(format(i, 'b'))
        if len(a) < n:
            a = "0" * (n - len(a)) + a
        map1.append(a)

    for i in arr2:
        a = str(format(i,'b'))
        if len(a) < n:
            a = "0"*(n-len(a))+a
        map2.append(a)

    for i in range(len(map1)):
        mapLine = ""
        for j in range(len(map1)):
            cnt = int(map1[i][j])+int(map2[i][j])
            if cnt >= 1:
                mapLine += "#"
            else:
                mapLine += " "

        answer.append(mapLine)

    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))