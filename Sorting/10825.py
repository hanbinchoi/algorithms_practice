num = int(input())
pointList = []

for i in range(num):
    a,b,c,d = input().split()
    pointList.append([a,int(b),int(c),int(d)])

pointList.sort(key = lambda x:(-x[1],x[2],-x[3],x[0]))

for a in pointList:
    print(a[0])