'''
1654 랜선 자르기
K개의 랜선을 잘라 N개의 길이가 같은 랜선으로 만들 때, 만들 수 있는 최대 랜선의 길이는?
제일 짧은 랜선의 길이대로 잘라보고, 잘린 나머지 랜선에 대해서 더 자를 수 있는지 확인해본다.
근데 제일 짧은 랜선을 사용하지 않고도 자를 수 있을 수 있다...
개수가 부족하면 길이를 줄이고, 넘치면 길이를 늘인다.
'''

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
        total += lan / mid

    if total < N:
        end = mid - 1

    else:
        start = mid + 1

print(end)
