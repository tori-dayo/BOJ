n, k = map(int, input().split())
array = list(map(int, input().split()))

plus = sum(array[:k])  
idx = 0
max_sum = plus  

for i in range(1, n - k + 1):
    plus = plus - array[i - 1] + array[i + k - 1]
    
    if plus > max_sum:
        max_sum = plus
        idx = i

print(max_sum)