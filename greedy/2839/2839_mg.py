n = int(input())
result = 0

while True:
    if n == 1 or n == 2:
        result = -1
        break
    if n % 5 == 0:
        result += n // 5
        break
    n-= 3
    result += 1

print(result)
