from collections import deque


def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)

computers = int(input())
node = int(input())
graph = [[] for _ in range(computers+1)]

for i in range(node):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()

visited = [False] * (computers+1)

bfs(graph,1,visited)
print(graph)
print(visited)
print(visited.count(True)-1)