num = int(input())
pointList = []

for i in range(num):
    a,b = map(int, input().split())
    pointList.append([b,a])
pointList.sort()
for i,j in pointList:
    print(j,i)