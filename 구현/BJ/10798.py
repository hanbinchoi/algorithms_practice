wordList =[]
for i in range(5):
    wordList.append(input())

word = ""

for i in range(15):
    for j in range(5):
        if len(wordList[j]) > i:
            word += wordList[j][i]


print(word)