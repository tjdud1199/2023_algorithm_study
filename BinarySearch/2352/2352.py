import sys
n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
lis = [0]

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


for x in arr:
    if lis[-1] < x:
        lis.append(x)
    else:
        lis[binary_search(x,0,len(lis))] = x

print(len(lis)-1)