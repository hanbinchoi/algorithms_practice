

a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print("*", sep='', end='')
    print()