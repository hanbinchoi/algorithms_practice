num = int(input())

for i in range(num):
    for j in range(i+1):
        if i==j:
            print("*")
        else:
            print("*",end='',sep='')