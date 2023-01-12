#만약에 리스트 내의 원소를 스플릿했을 때 + 값이 있으면 괄호를 치면 된다.
import re
n = input()
a = n.split('-')

for i in a:
    z = i.split('+')
    if len(z) > 1:
        z.append('(',0)
        z.append(')',-1)
    else:
        print(-1)