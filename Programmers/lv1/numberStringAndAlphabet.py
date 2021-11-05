
def solution(s):
    answer = []
    numDict = {
        "zero" : "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    now = 0
    next = 1
    while now < len(s):
        print(s[now:next])
        if s[now:next].isalpha():
            if s[now:next] in numDict.keys():
                answer.append(numDict[s[now:next]])
                now = next
                next = now + 1
            else:
                next += 1
        else:
            answer.append((s[now:next]))
            now = next
            next = now+1

    return int(''.join(answer))

print(solution("onenine4seveneight"))