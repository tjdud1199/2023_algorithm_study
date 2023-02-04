k = int(input())
array = []
result = 0
for x in range(k):
  x = int(input())
  if x != 0:
    array.append(x)
  else:
    del array[-1]

for i in array:
  result += i

print(result)