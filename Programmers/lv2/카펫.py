def solution(brown, yellow):
    answer = []
    aplusb = brown//2 + 2
    amulb = brown+yellow
    a = 1
    while True:
        b = aplusb - a
        print(a,b)

        if a*b == amulb:
            break
        a += 1
    return [b,a]

print(solution(10,2))