def solution(n):
    answer = ''
    a,b = n//3, n%3
    if b==0:
        a -= 1

    while a>=4:

    if b==0:
        a -= 1
        b = 4
    if a==3:
        a=4
    return str(a)+str(b)

print(solution(13))