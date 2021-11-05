def solution(new_id):
    answer = ""
    new_id = new_id.lower()
    character = "-_."
    new_id2 = ""
    for i in new_id:
        if i.isdigit() or i.isalpha() or i in character:
            new_id2+=i
    now = 0
    ispt = False

    while True:

        if ispt and new_id2[now] == '.':
            now += 1
        elif new_id2[now] == '.':
            ispt = True
            answer += new_id2[now]
            now += 1
        else:
            ispt = False
            answer += new_id2[now]
            now+= 1
        if now == len(new_id2): break

    answer = firstAndLastPoint(answer)
    if len(answer) == 0:
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
    answer = firstAndLastPoint(answer)
    while len(answer) <= 2:
        answer += answer[-1]
    return answer

def firstAndLastPoint(answer):
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[len(answer) - 1] == '.':
        answer = answer[:-1]
    return answer
print(solution("=.="))