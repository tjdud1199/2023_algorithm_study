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
