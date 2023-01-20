count = int(input()) # 입력받을 스택 리스트 안의 총 숫자의 수
stk = [] # 스택 리스트

for i in range(count): 
    num = int(input())
    if(num == 0): #num이 0이면 pop
        stk.pop()
    else:
        stk.append(num) #그게 아니라면 append = push
print(sum(stk))