n = int(input())
wine = [0] * (n+1)
for i in range(n):
    wine[i] = int(input())

d = [0] * (n+1)
d[0] = wine[0]
d[1] = wine[0] + wine[1]
d[2] = max(d[1], wine[2]+wine[0], wine[2]+wine[1])
for i in range(3,n):
    d[i] = max(d[i-1], wine[i]+d[i-2], wine[i]+wine[i-1]+d[i-3])

print(max(d))