def solution(n):
    answer = ''
    a,b = n//3, n%3
    add=""

    while a>=4:
        if b == 0:
            a -= 1
            b=4
        add += str(b)
        k = a
        a = a//3
        b = k%3

    if b==0:
        a -= 1
        b = 4
    if a==3:
        a=4
    if a==-1:
        a=0
    answer += str(a)+str(b)+add
    answer = answer.replace("0","")
    return answer

for i in range(100):
    print(i,"=",solution(i))