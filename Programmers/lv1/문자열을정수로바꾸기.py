def solution(s):
    answer = 0
    f = s[0]
    if f.isdigit():
        answer = int(f+s[1:])
    elif f == '-':
        answer = -1*int(s[1:])
    else:
        answer = int(s[1:])
    return answer

print(solution("1234"))