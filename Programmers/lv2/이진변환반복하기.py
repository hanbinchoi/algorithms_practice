def solution(s):
    cnt = 0
    zCnt = 0
    while s!="1":
        a = len(s)
        s = s.replace("0","")
        b = len(s)
        zCnt += a-b
        s = bin(len(s))[2:]
        cnt += 1
    return [cnt,zCnt]
print(solution("110010101001"))