k = int(input())

for x in range(k):
    n, m = map(int, input().split())
    i = list(map(int, input().split()))
    result = 0
    while m != -1:
        if i[0] == max(i):
            del i[0]
            m -= 1
            result += 1
        else:
            i.append(i[0])
            del i[0]

            if m == 0:
                m = len(i) - 1
            else:
                m -= 1
    print(result)