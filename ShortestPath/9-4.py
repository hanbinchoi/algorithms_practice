# n,m = map(int,input().split())
# INF = int(1e9)
# # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
# graph = [[INF] * (n) for _ in range(n)]
# # 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
# for a in range(n):
#     for b in range(n):
#         if a==b:
#             graph[a][b] = 0
# # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
# for _ in range(m):
#     # a에서 b로 가는 비용은 c로 초기화
#     a,b = map(int,input().split())
#     graph[a-1][b-1] = 1
#     graph[b-1][a-1] = 1
#
# for k in range(n):
#     for a in range(n):
#         for b in range(n):
#             graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
#
# x,k = map(int,input().split())
# dist = graph[0][k-1]+graph[k-1][x-1]
# if dist>INF:
#     print(-1)
# else:
#     print(dist)
#


n,m = map(int,input().split())
INF = int(1e9)
graph = [[INF]* n for _ in range(n)]
print(graph)

for i in range(n):
    for j in range(n):
        if i==j: graph[i][j] = 0

for i in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

x,k = map(int,input().split())

dist = graph[0][k-1]+graph[k-1][x-1]

if dist>INF: print(-1)
else: print(dist)
