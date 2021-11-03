def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    acnt,bcnt,ccnt = 0,0,0
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            acnt += 1
        if answers[i] == b[i % len(b)]:
            bcnt += 1
        if answers[i] == c[i % len(c)]:
            ccnt += 1
    maxcnt = max([acnt,bcnt,ccnt])
    if maxcnt == acnt:
        answer.append(1)
    if maxcnt == bcnt:
        answer.append(2)
    if maxcnt == ccnt:
        answer.append(3)

    return answer

print(solution([1,2,3,4,5]))