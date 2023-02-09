# 보석 도둑
# N개의 보석, 무게 M, 가격 V
# 가방 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 C, 가방에는 최대 한 개의 보석.
# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램
# 각 가방에 넣을 수 있는 보석 중 가장 비싼 것을 넣어야 함. 작은 가방에 보석을 먼저 넣어야 함.
# 가방을 무게로 오름차순 정렬, 적은 무게부터 확인. 보석은 무게로 정렬 후 가격으로 정렬

import sys
import heapq
from collections import deque
input = sys.stdin.readline

# 보석 개수, 가방 개수 입력
N, K = map(int, input().split())
jewels = []

for _ in range(N):
    M, V = map(int, input().split())
    jewels.append((M, V))

# 무게 기준 보석 정렬
jewels = deque(sorted(jewels, key = lambda x : x[0])) #무게에 대해 오름차순 정렬


# 가방 입력 후 정렬
bags = [int(input()) for _ in range(K)]
bags.sort()

# 힙 생성
heap = []
sum = 0

for weight in bags:
    while jewels and jewels[0][0] <= weight:
        heapq.heappush(heap, -jewels.popleft()[1])

    if heap:
        sum -= heapq.heappop(heap)

print(sum)

