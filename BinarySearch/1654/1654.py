n,k = map (int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

start = 1
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        total += (x // mid)
    if total < k:
        end = mid - 1
    else:
        start = mid + 1

print(end)



