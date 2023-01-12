exp = input().split("-")

result = 0

for i in exp[0].split("+"):
    result += int(i)

for i in exp[1:]:
    for j in i.split("+"):
        result -= int(j)

print(result)
