n = int(input())
array = list(map(int,input().split()))
a,b = map(int,input().split())
result = 0

for i in array:
    cnt = 1
    people = i - a

    if people <= 0:
        result += cnt
        continue

    cnt += (people + b - 1) // b
    result += cnt

print(result)