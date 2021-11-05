from copy import deepcopy


def solution(participant, completion):
    ans =""
    players = {}
    for i in participant:
        if i in players.keys():
            players[i] += 1
        else:
            players[i] = 1
    for i in completion:
        players[i] -= 1
    reverse_p = dict(map(reversed,players.items()))
    ans = reverse_p[max(players.values())]
    return ''.join(ans)

print(solution(["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"]))