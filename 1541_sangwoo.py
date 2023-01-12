#만약에 리스트 내의 원소를 스플릿했을 때 + 값이 있으면 괄호를 치면 된다.
import re
n = input()
a = n.split('-')

for i in a:
    z = i.split('+')
    if len(z) > 1:
        z.append('(')
        z.append(')')
    else:
        print(-1)

##답안
a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)