def solution(dirs):
    answer = 0
    moveDict = {"U":[0,1], "L":[-1,0], "R":[1,0], "D":[0,-1]}
    position = [0,0]
    visited = []
    stepRecord = list()
    nextP = [0,0]
    for i in dirs:
        nextP[0] = position[0] + moveDict[i][0]
        nextP[1] = position[1] + moveDict[i][1]
        if nextP[0]>5 or nextP[0]<-5 or nextP[1]>5 or nextP[1]<-5:
            continue
        path = position+nextP
        if path in visited:
            pass
        else:
            answer += 1
            visited.append(position+nextP)
            visited.append(nextP+position)
        position[0] = nextP[0]
        position[1] = nextP[1]
    return answer

print(solution("LULLLLLLU"))