def solution(board, moves):
    answer = 0
    dalls = []
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                if len(dalls)!= 0 and dalls[-1] == j[i-1]:
                    dalls.pop()
                    answer += 2
                else: dalls.append(j[i-1])
                j[i-1] = 0
                break
    print(dalls)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))