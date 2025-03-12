import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))
cnt = 0

for i in range(n-1, 0, -1):
    idx = i  
    for j in range(i-1, -1, -1):
        if array[j] > array[idx]:  
            idx = j
    
    if idx != i:
        array[i],array[idx] = array[idx],array[i]
        cnt += 1
        
    if cnt == k:
        print(*array)
        exit()
print(-1)