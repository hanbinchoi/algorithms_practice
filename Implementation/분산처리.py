n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    k = a%10
    if k == 0:
        print(10)
    elif k == 1:
        print(1)
    elif k == 2:
        base = [2,4,8,6]
        print(base[(b%4)-1])
    elif k == 3:
        base = [3,9,7,1]
        print(base[(b%4)-1])
    elif k == 4:
        base = [4,6]
        print(base[(b%2)-1])
    elif k == 5:
        print(5)
    elif k == 6:
        print(6)
    elif k == 7:
        base = [7,9,3,1]
        print(base[(b%4)-1])
    elif k ==8:
        base = [8,4,2,6]
        print(base[b%4-1])
    elif k == 9:
        base = [9,1]
        print(base[b%2-1])