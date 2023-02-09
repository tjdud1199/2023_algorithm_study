## boj 2805 : 나무자르기
> 문제 주소 : https://www.acmicpc.net/problem/2805
>
> 난이도 : silver 2

### 0. 문제
- 나무 M미터가 필요하며, H 높이를 지정해 나무를 절단한다.
- 나무를 필요한 만큼만 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하자

### 1. 문제 해결 방향
1. 나무를 자른 나머지 길이를 기준으로 더 자를지 덜 자를지 결정한다.

### 2. 소스코드
```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
result = 0
end = max(arr)

while start <= end:
    total = 0
    h = (start + end) // 2

    for tree in arr:
        if tree - h > 0:
            total += tree - h

    if total < m:
        end = h - 1

    else:
        result = h
        start = h + 1

print(result)

```

### 3. 알게된 점
- python으로 돌리니까 시간초과가 떴는데 pypy3로 돌리니까 성공했다