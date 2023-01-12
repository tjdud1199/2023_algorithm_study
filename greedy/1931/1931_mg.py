n = int(input())
time_table=[]

for _ in range(n):
    start, end = map(int, input().split())
    time_table.append((start, end))

time_table.sort(key = lambda x: x[0])
time_table.sort(key = lambda x : x[1])


result = 1
end_time = time_table[0][1]
for i in range(1,n):
    if time_table[i][0] >= end_time:
        result += 1
        end_time = time_table[i][1]

print(result)
