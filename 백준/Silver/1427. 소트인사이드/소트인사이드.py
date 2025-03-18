n = int(input())
array = list(str(n))
array.sort(reverse = True)
result = ''
for i in array:
    result += i

print(int(result))