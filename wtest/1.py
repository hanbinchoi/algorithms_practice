def solution(arr):
    acnt = arr.count(1)
    bcnt = arr.count(2)
    ccnt = arr.count(3)
    maxCnt = max(acnt,bcnt,ccnt)
    answer = [maxCnt-acnt,maxCnt-bcnt,maxCnt-ccnt]

    return answer

print(solution([]))