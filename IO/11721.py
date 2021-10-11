text = input()

for i in range(len(text)):
    print(text[i], end='')
    if (i%10==9):
        print()