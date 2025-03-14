def solution(a,b):
    a.sort()
    b.sort(reverse = True)
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result