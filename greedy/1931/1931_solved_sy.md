## boj 1931 : 회의실 배정
> 문제 주소 : https://www.acmicpc.net/problem/1931
>
> 난이도 : silver 1

### 0. 문제
- 하나의 회의실을 사용하려고 하는 N개의 회의 중, 겹치지 않게 할 수 있는 최대 회의 개수 구하기
- 시작 시간과 끝나는 시간이 같을 수 있다.


### 1. 문제 해결 방향
- 빨리 시작하고 일찍 끝나는 회의들을 배정한다.
- 시작시간 기준으로 정렬 후 끝나는 시간 기준으로 정렬한다.

### 2. 소스코드
```python
import sys
input = sys.stdin.readline
```
- 회의 시간표를 입력받아 튜플로 저장한다.
```python
# 입력받기
N = int(input())
times = []
for _ in range(N):
    a, b = map(int, input().split())
    times.append((a,b))
```
- 시간을 시작시간 기준으로 정렬 후, 끝나는 시간 기준으로 정렬한다.
- 한 번에 키를 두 개 주는 문법도 있던데, 그렇게 하면 안된다. 이유는 모르겠음
- 결과를 보면 정렬된 값이 결국 끝나는 시간 기준으로 정렬된 것이길래 끝나는 시간 기준으로만 정렬했는데도 틀렸음
```python
# 정렬하기
times.sort(key=lambda x:x[0])
times.sort(key=lambda x:x[1])
print(times)
end = 0
cnt = 0
```
- 정렬된 시간에 대해, 시작시간과 끝 시간을 비교해서 갱신한다. 조건에 맞으면 count 한다.
```python
for i, j in times:
    if i >= end:
        cnt += 1
        end = j

print(cnt)

```

### 3. 시간 초과 버전
```python
import sys
input = sys.stdin.readline

# 입력받기
N = int(input())
times = []
for _ in range(N):
    a, b = map(int, input().split())
    times.append((a,b))

# 정렬하기
times.sort(key=lambda x:(-x[1],-x[0]))
now = times[0]
cnt = 1

while times:
    start = now[0]
    end = now[1]
    for time in times:
        if start < time[1]:
            times.remove(time)
        else:
            now = time
            cnt += 1
            break

print(cnt)
```

#### 4. 알아둘 점
- map을 통하면 입력받을 때 형변환 하기 편하다
- sys 함수를 쓰면 입력 시간을 단축할 수 있다.
- 반복문은 되도록 쓰지 않도록 하자...