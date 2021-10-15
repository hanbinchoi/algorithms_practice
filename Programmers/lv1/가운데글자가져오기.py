def solution(s):
    answer = ''
    mid = len(s)//2
    print(mid)
    if len(s)%2 == 0:
        return s[mid-1:mid+1]
    else:
        return s[mid]

print(solution("abcde"))