from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ' )
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
point, node, start = map(int,input().split())
graph = [[] for _ in range(point+1)]

for i in range(node):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
visited = [False] * (point+1)
dfs(graph,start,visited)
visited = [False] * (point+1)
print()
bfs(graph,start,visited)
