def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        deploy = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i] != 0:
            deploy += 1
        answer.append(deploy)

    day = answer.pop(0)
    k=1
    result = []
    while answer:
        if day>=answer[0]:
            answer.pop(0)
            k += 1
        else:
            result.append(k)
            day = answer.pop(0)
            k=1
    result.append(k)
    return result

# print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]	))


print(solution([96,94],	[3,3]	))