k = input()
num = ""
intNum = []
for i in k:
    if i.isdigit():
        num += i
    else:
        intNum.append(num)
        intNum.append(i)
        num = ""
intNum.append(num)
print(intNum)
answer = 0
g = False
for i in intNum:
    if not g:
        if i.isdigit():
            answer += int(i)
        elif i == '-':
            g = True
        else:
            pass
    else:
        if i.isdigit():
            answer -= int(i)
        elif i == '-':
            pass
        else:
            pass
print(answer)