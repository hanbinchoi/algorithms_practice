import string

tmp = string.digits+string.ascii_uppercase

def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    cnt = 0
    answer = ""
    while True:
        answer += (convert(cnt,n))
        if len(answer) >= (t-1)*m+p:
            break
        cnt += 1

    answer = answer[:(t-1)*m+p]
    print(answer)
    k=0
    result = ""
    print(len(answer))
    while k!=t:
        result += answer[(p-1)+k*m]
        print(p+2*k)
        k += 1

    return result
print(solution(16, 16, 2, 2))