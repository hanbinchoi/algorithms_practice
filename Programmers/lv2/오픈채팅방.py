def solution(record):
    answer = []
    idDict = dict()
    log = []
    for i in record:
        data = i.split()
        log.append((data[0],data[1]))
        if data[0] == "Enter" or data[0] == "Change":
            idDict[data[1]] = data[2]

    for i in log:
        if i[0] == "Enter":
            answer.append(idDict[i[1]]+"님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(idDict[i[1]]+"님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))