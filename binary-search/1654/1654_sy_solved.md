## boj 1654 : 랜선 자르기
> 문제 주소 : https://www.acmicpc.net/problem/1654
>
> 난이도 : silver 2

### 0. 문제
- 캠프 때 쓸 N개의 랜선 만들기
- K개의 길이가 제각각인 랜선을 N개의 같은 길이의 랜선으로 만들기
- N개보다 많이 만드는 것도 N개를 만드는 것에 포함이 된다
- 만들 수 있는 랜선의 최대 길이는?

### 1. 문제 해결 방향
1. 가장 긴 랜선의 절반 길이부터 시작해서 계속 잘라본다.
2. 자른 개수가 부족하면 자를 길이를 줄이고, 넘치면 자를 길이를 늘인다.

### 2. 소스코드
```python
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

start = 0
end = max(arr)

while start <= end:
    total = 0
    mid = (start + end + 1) // 2
    for lan in arr:
        total += lan // mid

    if total < N:
        end = mid - 1

    else:
        start = mid + 1

print(end)
```

### 3. 알게된 점
- mid = (start + end)//2 로 구현하면 ZeroDivisionError에 걸린다.
- mid가 0이 될 수 있어서 total을 계산할 때 문제가 생겼다.