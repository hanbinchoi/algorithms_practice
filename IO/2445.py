num = int(input())

for i in range(num):
    for j in range(num * 2):
        if i >= j or j >= (num * 2 - i - 1):
            print("*", end='', sep='')
        else:
            print(" ", end='', sep='')
    print()

for i in range(num-1):
    for j in range(num * 2):
        if j >= (num-i-1) and j <= (num+i):
            print(" ", end='', sep='')
        else:
            print("*", end='', sep='')
    print()
