def solution(n):
    answer = 0
    convert = []
    if n < 3:
        return n
    while n>0:
        convert.append(n%3)
        n =n//3

    convert.reverse()
    for i in range(len(convert)):
        answer += 3**i * convert[i]

    return answer

print(solution(29))
