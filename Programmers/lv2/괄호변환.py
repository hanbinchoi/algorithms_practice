def solution(p):
    answer = ''
    text = ""
    cnt = 0
    for i in p:
        if i == p[0]:
            text += i
        elif text[-1] == i:
            break
        cnt += 1
    u = text
    v = p[cnt-1:]
    print(u,v)

    return answer

print(solution("(()())()"))