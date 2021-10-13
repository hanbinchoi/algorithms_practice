import sys

list = []

num = int(sys.stdin.readline())

for _ in range(num):
    data = sys.stdin.readline().split()

    if data[0] == 'push':
        list.append(int(data[1]))

    elif data[0] == 'front':
        if len(list)==0:
            print(-1)
        else:
            print(list[0])

    elif data[0] == 'back':
        if len(list)==0:
            print(-1)
        else:
            print(list[-1])

    elif data[0] == 'size':
        print(len(list))

    elif data[0] == 'pop':
        if len(list)==0:
            print(-1)
        else:
            print(list.pop(0))

    elif data[0] == 'empty':
        if len(list)==0:
            print(1)
        else:
            print(0)
