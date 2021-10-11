num = int(input())
pointList = []

for i in range(num):
    a,b = map(int, input().split())
    pointList.append([a,b])


def merge_sort(pList):
    if len(pList) <= 1:
        return pList
    mid = len(pList) // 2
    left = pList[:mid]
    right = pList[mid:]

