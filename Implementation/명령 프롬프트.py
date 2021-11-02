n = int(input())
texts = []
for i in range(n):
    texts.append(input())

text = texts.pop(0)
index = set()
for i in texts:
    if text == texts:
        continue
    else:
        for j in range(len(i)):
            if text[j] != i[j]:
                index.add(j)
text = list(text)

for i in index:
    text[i] = "?"

s = "".join(text)

print(s)
