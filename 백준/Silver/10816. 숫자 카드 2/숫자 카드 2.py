from bisect import bisect_left , bisect_right

n = int(input())
array = list(map(int,input().split()))

m = int(input())
target = list(map(int,input().split()))

result = []
array.sort()

def count_number(array,x):
    left_number = bisect_left(array,x)
    right_number = bisect_right(array,x)
    return right_number - left_number

for i in target:
    result.append(count_number(array,i))

print(*result)