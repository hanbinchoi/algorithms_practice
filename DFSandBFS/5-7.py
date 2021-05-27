graph = [[] for _ in range(3)]

# 0 에 연결된 노드와 거리
graph[0].append((1,7))
graph[0].append((2,5))

# 1 에 연결된 노드와 거리
graph[1].append((0,7))

# 2 에 연결된 노드와 거리
graph[2].append((0,5))



print(graph)