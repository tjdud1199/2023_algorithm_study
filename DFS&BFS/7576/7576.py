from collections import deque
m,n = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])


def bfs():
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y

            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

result = 0
bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result-1)