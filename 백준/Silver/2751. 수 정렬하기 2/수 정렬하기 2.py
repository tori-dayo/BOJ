import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    x = int(input())
    result.append(x)
result.sort()
for i in result:
    print(i)