def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    return answer

print(solution("1234"))