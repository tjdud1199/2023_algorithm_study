n = int(input())
array = list(map(int,input().split()))
lis = [0 for _ in range(n)]
for i in range(n):
  for j in range(i):
    if array[i] > array[j] and lis[i] < lis[j]:
      lis[i] = lis[j]
  lis[i] += 1

print(max(lis))