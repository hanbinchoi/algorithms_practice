def solution(log):
    answer = 0
    now = 0
    while now <= len(log)-1:
        s_hour = int(log[now][:2])
        s_miniute = int(log[now][3:])
        e_hour = int(log[now+1][:2])
        e_miniute = int(log[now+1][3:])
        time = (e_hour-s_hour)*60 + (e_miniute-s_miniute)
        if time<5:
            time = 0
        elif time>105:
            time = 105
        answer += time
        now+=2
    hour = answer//60
    minute = answer%60
    answer = str(hour).zfill(2)+":"+str(minute).zfill(2)
    return answer

print(solution(["18:30","20:16"]))