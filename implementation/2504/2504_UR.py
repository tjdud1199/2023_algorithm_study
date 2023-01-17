bracket = input()
stack = []
step = 1
result = 0

for i in range(len(bracket)):
    b = bracket[i]

    if b == '(':
        stack.append(b)
        step *= 2

    elif b == ')':
        if stack[-1] != '(' or len(stack) == 0:
            result = 0
            break
        if bracket[i - 1] == '(':
            result += step
        stack.pop()
        step //= 2

    elif b == '[':
        stack.append(b)
        step *= 3

    elif b == ']':
        if stack[-1] != '[' or len(stack) == 0:
            result = 0
            break
        if bracket[i - 1] == '[':
            result += step
        stack.pop()
        step //= 3

print(result)
