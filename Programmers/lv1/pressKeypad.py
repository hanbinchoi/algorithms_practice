def solution(numbers, hand):
    answer = ''
    lnow = 10
    rnow = 12
    ptDict = {
        1: [1, 1],
        2: [1, 2],
        3: [1, 3],
        4: [2, 1],
        5: [2, 2],
        6: [2, 3],
        7: [3, 1],
        8: [3, 2],
        9: [3, 3],
        10: [4, 1],
        11: [4, 2],
        12: [4, 3]

    }
    for i in numbers:
        if i == "*": i = 10
        if i == "#": i = 12
        if i == 0: i = 11

        if i == 1 or i == 4 or i == 7 or i == 10:
            answer += "L"
            lnow = i
        elif i == 3 or i == 6 or i == 9 or i == 12:
            answer += "R"
            rnow = i
        else:
            pt = ptDict[i]
            lpt = ptDict[lnow]
            rpt = ptDict[rnow]
            ldist = abs(pt[0]-lpt[0])+abs(pt[1]-lpt[1])
            rdist = abs(pt[0]-rpt[0])+abs(pt[1]-rpt[1])
            print("dis",i,ldist,rdist)
            if ldist>rdist:
                answer += "R"
                rnow = i
            elif ldist<rdist:
                answer += "L"
                lnow = i
            else:
                if hand == "right":
                    answer += "R"
                    rnow = i
                else:
                    answer += "L"
                    lnow = i
        print(lnow,rnow)
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))