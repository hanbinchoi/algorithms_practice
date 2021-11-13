def solution(s):
    idx = [0]
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            idx.append(i+1)
    idx.append(len(s))

    texts = []
    for i in range(len(idx)-1):
        texts.append(s[idx[i]:idx[i+1]])
    print(texts)
    lens = []
    if texts[0][0] == texts[-1][0]:
        lens.append(len(texts[0]+texts[-1]))
        texts.pop(0)
        texts.pop()
    for i in texts:
        lens.append(len(i))
    lens.sort()
    return lens

print(solution("a"))