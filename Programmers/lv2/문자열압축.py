def solution(s):
    answer = 1001
    shortS = ""
    temp = ""
    cnt = 1
    for i in range(1,len(s)):
        for j in range(0,len(s),i):
            if j==0:
                temp = s[j:j+i]
            elif temp != s[j:j+i]:
                if cnt == 1:
                    shortS += temp
                else:
                    shortS += str(cnt) + temp
                temp = s[j:j+i]
                cnt = 1
            else:
                cnt += 1
        if cnt == 1:
            shortS += temp
        else:
            shortS += str(cnt)+temp
        print(shortS)
        if answer > len(shortS):
            answer = len(shortS)
        shortS = ""
        temp = ""
        cnt = 1
    if answer == 1001:
        return len(s)
    return answer

print(solution("xxxxxxxxxxyyy"))