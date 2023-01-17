k = int(input())
cog = []
for i in range(k):
  money = int(input())
  if money == 0:
    cog.pop(-1)
  else:
    cog.append(money)
print(sum(cog))
