# n = int(input())
#
# data = list(map(int,input().split()))
# data = data[:n]
# data.sort()
#
# m = int(input())
#
# target = list(map(int,input().split()))
# target = target[:m]

# def binary_search(data,target,start,end):
#     if start>end: return None
#
#     mid = (start+end) // 2
#
#     if data[mid]==target: return True
#     if data[mid] > target:
#         return binary_search(data, target, start, mid-1)
#
#     if data[mid] < target:
#         return binary_search(data, target, mid+1, end)
#

# def binary_search(data,target,start,end):
#     while start<=end:
#         print(start,end)
#         mid = (start+end) // 2
#         if(data[mid] == target): return True
#
#         elif data[mid]>target:
#             end = mid-1
#         elif data[mid]<target:
#             start = mid+1
#     return False
#
# for i in range(len(target)):
#     if(binary_search(data,target[i],0,len(data)-1)): print("yes",end=' ')
#     else: print("no",end=' ')

n = int(input())

A = list(map(int,input().split()))
A = A[:n]
A.sort()

m = int(input())

B = list(map(int,input().split()))
B = B[:m]

def binary_search(data,target,start,end):
    while(start<=end):
        mid = (start+end) // 2

        if data[mid] == target:
            return True
        elif data[mid] > target:
            end = mid-1
        elif data[mid] < target:
            start = mid+1
    return False

for i in range(len(B)):
    if binary_search(A,B[i],0,n-1): print("yes",end=' ')
    else: print("no", end=' ')