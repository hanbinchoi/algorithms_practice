def solution(time, plans):
    answer = ""
    mon = [13, 18]
    fri = [9.5, 18]
    temp = []
    for i in plans:
        ampm = ""
        temp_time = ""
        d_time = i[1]
        for j in d_time:
            if not j.isdigit():
                ampm += j
            else:
                temp_time += j
        if (ampm == "PM"and temp_time != "12"):
            d_temp_time = int(temp_time) + 12
        elif (ampm=="AM" and temp_time == "12"):
            d_temp_time = 0
        else:
            d_temp_time = int(temp_time)

        a_time = i[2]
        ampm = ""
        temp_time = ""
        for j in a_time:
            if not j.isdigit():
                ampm += j
            else:
                temp_time += j
        if (ampm == "PM"and temp_time != "12"):
            a_temp_time = int(temp_time) + 12
        elif (ampm == "AM" and temp_time == "12"):
            a_temp_time = 0
        else:
            a_temp_time = int(temp_time)
        temp.append([i[0],d_temp_time,a_temp_time])
    print(temp)
    for i in temp:
        need = 0
        if i[1]<=fri[1]:
            if i[1] <= fri[0]:
                need += fri[1]-fri[0]
            else:
                need += fri[1]-i[1]
        if i[2]>=mon[0]:
            if i[2] >= mon[1]:
                need += mon[1]-mon[0]
            else:
                need += i[2]-mon[0]
        if need < time:
            answer = i[0]
        print(need)
    return answer

print(solution(3.5,[["홍콩", "12PM", "12PM"] ]))