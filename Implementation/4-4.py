n,m = map(int,input().split())
a,b,d = map(int,input().split())

field = list()

direction = [0,1,2,3]
step = [(-1,0),(0,1),(1,0),(0,-1)]
count = 0

for i in range(n):
    field.append(list(map(int,input().split())))

while(True):
    if(field[a][b] == 0):
        count += 1
        if(d == 0): d=4
        na = a+step[direction[d-1]][0]
        nb = a+step[direction[d-1]][1]
        field[na][nb]
        print(na,nb)
print(field[1][1])