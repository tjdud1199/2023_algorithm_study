result_list = []
test_case = int(input())
for _ in range(test_case):
  n, m = map(int,input().split())
  imp = list(map(int,input().split()))
  idx = list(range(len(imp)))
  idx[m] = 'target'

  result = 1
  while True:
    if imp[0] == max(imp):
      if idx[0] == 'target':
        result_list.append(result)
        break
      else:
        result += 1
        imp.pop(0)
        idx.pop(0)
    else:
      imp.append(imp.pop(0))
      idx.append(idx.pop(0))  

for i in range(test_case):
  print(result_list[i])