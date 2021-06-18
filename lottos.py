def solution(lottos, win_nums):
    answer = []
    count = 0
    z_count = 0
    lottos.sort()
    win_nums.sort()
    for i in lottos:
        if i in win_nums: count += 1
        elif i == 0: z_count += 1
    rank = [6,6,5,4,3,2,1]
    answer.append(rank[(count+z_count)])
    answer.append(rank[count])

    return answer

print(solution([44,1,0,0,31,25],[31,10,45,1,6,19]))

dd