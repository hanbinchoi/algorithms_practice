def solution(a, b):
    answer = 0
    monthDays = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    dayFrequency = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    mon = a-1
    day = b-1

    for i in range(mon):
        answer+=monthDays[i+1]
    answer+=day
    return dayFrequency[answer%7]

print(solution(5, 24))