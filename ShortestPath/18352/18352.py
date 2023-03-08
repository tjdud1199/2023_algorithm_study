import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))

def dijkstra(graph, start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [distance[start], start])

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

dist_start = dijkstra(graph,x)
find = False
for idx, i in enumerate(dist_start):
    if i == k:
        print(idx)
        find = True
if not find:
    print(-1)


