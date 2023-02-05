from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        y = queue.popleft()
        for i in graph[y]:
            if visited[i] == 0:
                visited[i] = -visited[y]
                queue.append(i)
            else:
                if visited[i] == visited[y]:
                    return False
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    flage = 1
    for j in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(v+1):
        if visited[i] == 0:
            if not bfs(i):
                flag = -1
                break
    if flag == 1: print('YES')
    else: print('NO')