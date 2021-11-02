from copy import deepcopy


def solution(participant, completion):
    d = dict()
    ans =""
    for i in participant:
        d[i] = 0
    for i in participant:
        if i in completion:
            d[i] += 1

    for keys,value in d.items():
        if value != 1:
            ans += keys
    return ans

print(solution(["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"]))