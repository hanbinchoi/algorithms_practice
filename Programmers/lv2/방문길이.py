def solution(dirs):
    answer = 0
    moveDict = {"U":[0,1], "L":[-1,0], "R":[1,0], "D":[0,-1]}
    position = [0,0]
    visited = set()
    stepRecord = list()
    for i in dirs:
        move = moveDict[i]
        if (position[0], position[1], move[0], move[1]) in visited:
            print("vis")
            continue

        if position[0]+move[0]>5 or position[1]+move[1]>5 or position[0]+move[0]<-5 or position[1]+move[1]<-5:
            print("max")
            continue

        visited.add((position[0], position[1], move[0], move[1]))
        visited.add((position[0]+move[0], position[1]+move[1], -move[0], -move[1]))
        answer += 1

    print(visited)
    return answer

print(solution("LULLLLLLU"))