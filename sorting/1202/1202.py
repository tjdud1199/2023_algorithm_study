import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
gem = []
for _ in range(n):
    weight, cost = map(int, input().split())
    heapq.heappush(gem, (weight, cost))

bags = []
for _ in range(k):
    w = int(input())
    bags.append(w)

bags.sort()
result = 0
temp = []
for bag_weight in bags:
    while gem:
        if bag_weight >= gem[0][0]:
            weight, cost = heapq.heappop(gem)
            heapq.heappush(temp, -cost)
        else:
            break

        if temp:
            result -= heapq.heapop(temp)

print(result)