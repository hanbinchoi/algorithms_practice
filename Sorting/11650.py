num = int(input())
pointList = []

for i in range(num):
    a,b = map(int, input().split())
    pointList.append([a,b])
pointList.sort()
for i,j in pointList:
    print(i,j)