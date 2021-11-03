from itertools import permutations, combinations


def solution(number, k):
    answer = ''
    nList = list(number)
    nElem = list(combinations(nList,len(number)-k))
    m = 0
    for i in nElem:
        mv = ""
        for j in i:
            mv += j
        if m<int(mv):
            m = int(mv)
    return str(m)

print(solution("1924",2))