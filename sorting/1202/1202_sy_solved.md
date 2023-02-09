# 1202 보석도둑
> 문제 주소: https://www.acmicpc.net/problem/1202
> 
> gold 2

## 1. 문제
- N개의 보석이 있으며, 각각은 M의 무게와 V의 가격을 가진다
- 각각 최대 하나의 보석을 담을 수 있는 K개의 가방이 있으며, 각 가방에 담을 수 있는 최대 무게는 C
- 훔칠 수 있는 보석의 최대 가격은?

## 2. 문제 해결 방향
1. 각 가방에 넣을 수 있는 보석 중 가장 비싼 것을 넣어야 하며, 최대 무게가 있으므로 가벼운 가방을 먼저 채운다.
2. 작은 가방부터 채우며, 가능한 보석 중 비싼 것을 넣는다.
3. 작은 가방에 들어가는 보석은 더 무거운 가방에는 당연히 들어가므로, heap에 넣어두고 계속 확인한다.
- heapq란? 파이썬에서 제공하는 min heap으로, 인덱스 0 위치에 가장 작은 값이 들어가도록 정렬된다.
4. 음수값으로 넣어 max heap으로 사용한다.

## 3. 코드
```python
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
```
## 4. 알게된 점
- 음수값을 통해 max heap을 사용할 수 있다.
- deque로 정렬하면 시간이 더 짧게 걸린다.
