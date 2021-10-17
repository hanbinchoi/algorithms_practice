def solution(s):
    wait = True
    answer =""
    for i in range(len(s)):
        if s[i] ==" ":
            wait = True
            answer += s[i]
        else:
            if wait:
                answer += s[i].upper()
                wait = False
            else:
                wait = False
                answer += s[i].lower()
    return answer
print(solution("a   bcd   hello"))