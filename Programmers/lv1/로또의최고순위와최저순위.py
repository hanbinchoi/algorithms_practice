def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]
    cnt = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            win_nums.remove(i)
    high = (6-len(win_nums)+cnt)
    low = 6-len(win_nums)
    if high > 6: high = 6
    if low < 0: low = 0
    answer.append(rank[high])
    answer.append(rank[low])
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]	))