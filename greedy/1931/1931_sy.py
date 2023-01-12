'''
- 끝나는 시간 기준으로 내림차순 정렬한다.
- 시작 시간 기준으로 오름차순 정렬한다.
- 시작 시간보다 끝나는 시간이 이른 것 중, 끝나는 시간이 늦은 것을 선택한다.
'''

import sys
input = sys.stdin.readline

# 입력받기
N = int(input())
times = []
for _ in range(N):
    a, b = map(int, input().split())
    times.append((a,b))

# 정렬하기
times.sort(key=lambda x:x[0])
times.sort(key=lambda x:x[1])
print(times)
end = 0
cnt = 0

for i, j in times:
    if i >= end:
        cnt += 1
        end = j

print(cnt)
