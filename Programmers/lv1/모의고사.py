def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    acnt,bcnt,ccnt = 0,0,0
    cnt = 0
    for i in answers:
        if i == a[cnt % 5]: acnt += 1
        if i == b[cnt % 8]: bcnt += 1
        if i == c[cnt % 10]: ccnt += 1
        cnt += 1
    maxVal = max(acnt,bcnt,ccnt)

    if maxVal == acnt: answer.append(1)
    if maxVal == bcnt: answer.append(2)
    if maxVal == ccnt: answer.append(3)

    return answer

print(solution([1,2,3,4,5]))