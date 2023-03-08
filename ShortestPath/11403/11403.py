n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

for row in graph:
    for col in row:
        print(col, end=" ")
    print()