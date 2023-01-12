data = input()
data = data.split('-')
result = sum(map(int, data[0].split('+')))
for i in data[1:]:
  result -= sum(map(int, i.split('+')))
print(result)
