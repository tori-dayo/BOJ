n = int(input())
result = []
for _ in range(n):
    x = int(input())
    if x not in result:
        result.append(x)
result.sort()

for i in result:
    print(i)