def solution(weights, head2head):
    answer = []
    record = {}
    for i in range(len(weights)):
        win = 0
        lose = 0
        overWeight = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'W':
                win += 1
                if weights[i] < weights[j]:
                    overWeight += 1
            elif head2head[i][j] == 'L':
                lose += 1
        if win+lose == 0:
            record[i+1] = [weights[i],0,overWeight]
        else:
            record[i+1] = [weights[i],win/(win+lose),overWeight]
    record = sorted(record.items(), key=lambda x:(-x[1][1],-x[1][2],-x[1][0]))
    for i in record:
        answer.append(i[0])
    return answer

print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))