def solution(name):
    answer = 0
    nList = list(name)
    asc = []
    for i in nList:
        asc.append(ord(i))
    now = "A"*len(name)
    index = 0
    while True:
        if now == name:
            break
        if now[index] == name[index]:
            index += 1
            continue
        nowVal = min([ord(name[index]) - ord("A"),ord("Z")-ord(name[index])])
        if index != 0:
            preVal = min([ord(name[index]) - ord("A"),ord("Z")-ord(name[index])]) +1
        else:
            preVal = min([ord(name[len(name)-1]) - ord("A"),ord("Z")-ord(name[len(name)-1])]) +1
        if index != len(name)-1:
            nextVal = min([ord(name[index + 1]) - ord("A"), ord("Z") - ord(name[index + 1])]) + 1
        else:
            nextVal = min([ord(name[0]) - ord("A"), ord("Z") - ord(name[0])]) + 1
        maxVal = max([preVal,nextVal,nowVal])
        if nowVal == maxVal:
            now[index] = name[index]
            index += 1
            answer += nowVal
        elif preVal == maxVal:
            if index == 0:
                index = len(name)-1
                now[index] = name[index]
                answer += preVal
            else:
                index -= 1
                now[index] = name[index]
                answer += preVal

        elif nextVal == maxVal:
            if index != len(name) - 1:
                index += 1
                now[index] = name[index]
                answer += maxVal
            else:
                index = 0
                now[index] = name[index]
                answer += maxVal
    return answer

print(solution("JEROEN"))