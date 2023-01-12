num = int(input())
total = []
for _ in range(num):
  m = list(map(int,input().split()))
  total.append(m)
total.sort(key = lambda x :(x[1], x[0]))

result = [[0,0]]
for i in range(len(total)):
  if result[-1][1] <= total[i][0]:
    result.append(total[i])
print(len(result)-1)
