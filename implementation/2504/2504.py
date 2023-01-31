n = list(input())

array = []
temp = 1
result = 0

for i in range(len(n)):
    if n[i] == "[":
        array.append(n[i])
        temp *= 3

    elif n[i] == "(":
        array.append(n[i])
        temp *= 2

    elif n[i] == "]":
        if not array or array[-1] != '[':
            result = 0
            break
        if n[i - 1] == '[':
            result += temp
        array.pop()
        temp //= 3

    else:
        if not array or array[-1] != '(':
            result = 0
            break
        if n[i - 1] == '(':
            result += temp
        array.pop()
        temp //= 2

if array:
    result = 0

print(result)