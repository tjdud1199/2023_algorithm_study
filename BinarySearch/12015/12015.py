n = int(input())
array = list(map(int, input().split()))
lis = [0]

def binary_search(target, start, end):
    while start < end:
        mid = (start + end) // 2

        if lis[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

for i in array:
    if lis[-1] < i:
        lis.append(i)
    else:
        lis[binary_search(i,0,len(lis)-1)] = i

print(len(lis)-1)




