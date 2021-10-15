def solution(scores):
    answer = ''
    new_list = list(map(list, zip(*scores)))
    for i in range(len(new_list)):
        hasRedundancy = False

        if new_list[i].count(new_list[i][i]) > 1:
            hasRedundancy = True

        if not hasRedundancy:
            if max(new_list[i]) == new_list[i][i] or min(new_list[i]) == new_list[i][i]:
                avg = (sum(new_list[i])-new_list[i][i]) / (len(new_list[i])-1)
            else:
                avg = sum(new_list[i]) / len(new_list[i])
        else:
            avg = sum(new_list[i]) / len(new_list[i])

        if avg >= 90:
            answer += "A"
        elif avg >= 80:
            answer += "B"
        elif avg >= 70:
            answer += "C"
        elif avg >= 50:
            answer += "D"
        else:
            answer += "F"

    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))