n,m = map(int,input().split())
array = list(map(int,input().split()))

result = []

def count_result(array,mid,m):
    cnt,sum = 1,0

    for i in array:
        sum += i
        if sum > mid:
            cnt += 1
            sum = i
    if cnt > m:
        return False
    return True
            
def binary_search(array,start,end):
    if start > end:
        return None

    mid = (start + end) // 2

    if count_result(array,mid,m) == True:
        result.append(mid)
        binary_search(array,start,mid-1)
    else:
        binary_search(array,mid+1,end)
    
        
binary_search(array,max(array),sum(array))

print(min(result))