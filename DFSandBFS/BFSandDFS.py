from collections import deque


def dfs(graph,v,visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, v, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True

    while queue:
        # 큐에서 원소를 하나씩 뽑아 출력
        v= queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접요소들은 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        print(queue)
point, node, start = map(int,input().split())
graph = [[] for i in range(point+1)]

for i in range(node):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (point+1)

dfs(graph,start,visited)
print()
visited = [False] * (point+1)

bfs(graph,start,visited)