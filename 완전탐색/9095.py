def find(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return find(n-3)+find(n-2)+find(n-1)

n = int(input())

for i in range(n):
    print(find(int(input())))
