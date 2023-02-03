#1744 - 수를 합이 최대가 나오게 묶었을 때 합을 출력한다.
#수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.
#예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다.
#하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(23)+(45) = 27이 되어 최대가 된다.
#해당 문제는 수 묶기의 규칙을 찾는 것이 중요한 문제이다.

찾은 규칙은 다음과 같다.
#최대한 음수는 없애주고 양수는 살려주면 됨.
0, 양수 = 덧셈
0, 음수 = 곱셈

1, 양수 = 덧셈
1, 음수 = 덧셈
즉, 1 = 덧셈

양수, 양수 = 곱셈
음수, 음수 = 곱셈
양수, 음수 = 덧셈

양수 리스트는 내림차순 정렬,#내림차순으로 정리해서 큰 수끼리 곱셈
음수 리스트는 오름차순 정렬을 해준다.
해당 리스트의 길이가 짝수이면 리스트의 숫자를 2개씩 곱해주면 최댓값이 나온다.
홀수이면 마지막 숫자를 빼고 2개씩 곱해주고 마지막 수를 더해준다.

1 같은 경우 곱셈을 하면 최댓값이 안나오기 때문에 값에 그냥 1을 더해준다.

import sys

input = sys.stdin.readline

N = int(input())
positive = []  # 양수를 저장할 리스트
negative = []  # 음수를 저장할 리스트
max_sum = 0

for _ in range(N):
    n = int(input())

    if n > 1:
        positive.append(n)
    elif n == 1:
        max_sum += 1  # 1, 양수의 규칙에 의해 1을 더한다.
    else:
        negative.append(n)

positive.sort(reverse=True)  # 양수의 큰 수부터 정렬한다.
negative.sort()  # 음수의 작은 수부터 정렬한다.

# 양수 리스트 더해주기
if len(positive) % 2 == 0:  # 양수가 짝수개 일경우 두개씩 곱해준다.
    for i in range(0, len(positive), 2):
        max_sum += positive[i] * positive[i + 1]
else:
    for i in range(0, len(positive) - 1, 2):
        max_sum += positive[i] * positive[i + 1]
    max_sum += positive[len(positive) - 1]  # 마지막 수는 더해준다.

# 음수 더해주기
if len(negative) % 2 == 0:  # 음수가 짝수개 일경우 두개씩 곱해준다.
    for i in range(0, len(negative), 2):
        max_sum += negative[i] * negative[i + 1]
else:
    for i in range(0, len(negative) - 1, 2):
        max_sum += negative[i] * negative[i + 1]
    max_sum += negative[len(negative) - 1]  # 마지막 수는 더해준다.

print(max_sum)