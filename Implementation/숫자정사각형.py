a,b = map(int,input().split())
graph = []
for i in range(a):
    graph.append(list(input()))
ans = 1
for i in range(len(graph)):
    for j in range(len(graph[i])):
        pt = graph[i][j]
        for w in range(1,len(graph[i])):
            if i+w < len(graph) and j+w < len(graph[i]):
                if graph[i+w][j] == pt and graph[i][j+w] == pt and graph[i+w][j+w] == pt:
                    if ans < (w+1)*(w+1):
                        ans = (w+1)*(w+1)

print(ans)