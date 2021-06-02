# import sys
# import heapq
#
# input = sys.stdin.readline
# n, m, c = map(int,input().split())
# INF = int(1e9)
#
# graph = [[] for i in range(n)]
# distance = [INF] * n
#
# for i in range(m):
#     a, b, z = map(int, input().split())
#     graph[a-1].append((b-1,z))
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
# dijkstra(c-1)
#
# count = 0
# max_distance = 0
#
# for d in distance:
#     if d != INF:
#         count +=1
#         max_distance = max(max_distance,d)
#
# print(count-1, max_distance)

import sys
import heapq

# input = sys.stdin.readline
# INF = int(1e9)
#
# n,m,c = map(int,input().split())
#
# graph = [[] for _ in range(n)]
#
# distance = [[INF] for _ in range(n)]
#
# for i in range(m):
#     x,y,z = map(int,input().split())
#     graph[x-1].append(((y-1),z))
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#
#     while q:
#         now, dist = heapq.heappop(q)
#         if dist > distance[now]: continue
#
#         for i in graph[now]:
#             cost = dist + i
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dijkstra(c-1)
# count = 0
# for i in distance:
#     if i != INF:
#        count +=1
# print(count-1,max(distance))

INF = int(1e9)
input = sys.stdin.readline

n,m,c = map(int,input().split())

graph = [[] for i in range(n)]

distance = [INF] * n

for i in range(m):
    x,y,z = map(int,input().split())
    graph[x-1].append((y-1,z))

print(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]: continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(i[1],i[0]))

dijkstra(c-1)
count = 0
for i in range(len(distance)):
    if i != INF:
        count += 1

print(count-1,max(distance))