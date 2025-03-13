n,m = map(int,input().split())
array = list(map(int,input().split()))

start , end = max(array) , sum(array)

def binary_search(array,start,end):
    while start <= end:
        cnt = 1
        result = 0

        mid = (start + end) // 2

        for i in array:
            result += i
            if result > mid:
                cnt += 1
                result = i

        if cnt <= m:
            end = mid - 1
        else:
            start = mid + 1
    return start

binary_search(array,start,end)
print(binary_search(array,start,end))