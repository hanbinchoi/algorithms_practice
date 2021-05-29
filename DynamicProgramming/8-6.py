# n = int(input())
# d = [0] * n
# data = list(map(int,input().split()))
# data = data[:n]
# answer = 0
#
# d[0] = data[0]
# d[1] = max(data[0], data[1])
# for i in range(2,n):
#     d[i] = max(d[i-1],d[i-2]+data[i])
#
# print(d)
# print(d[n-1])
#
# n = int(input())
# data = list(map(int,input().split()))
# data = data[:n]
# d = [0] * n
#
# d[0] = data[0]
# d[1] = max(d[0],data[1])
#
# for i in range(2,n):
#     d[i] = max(d[i-1],d[i-2]+data[i])
#
# print(d[n-1])

n = int(input())
data = list(map(int,input().split()))
data = data[:n]
d = [0] * n

d[0] = data[0]
d[1] = max(d[0],data[1])

for i in range(2,n):
    d[i] = max(d[i-2]+data[i],d[i-1])

print(d[n-1])