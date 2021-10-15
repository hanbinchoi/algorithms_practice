def solution(N, stages):
    answer = []
    failRate = {}
    stages.sort()
    stage_set = set(stages)
    for i in range(1,N+1):
        failRate[i] = 0
    for i in stage_set:
        if i == N+1:
            break
        stay = stages.count(i)

        rate = stay / len(stages)
        while i in stages:
            stages.remove(i)  # 'Smith' 삭제

        failRate[i] = rate

    failRate = sorted(failRate.items(),reverse=True,key=lambda item:item[1])
    for i in failRate:
        answer.append(i[0])
    return answer[:N]

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))