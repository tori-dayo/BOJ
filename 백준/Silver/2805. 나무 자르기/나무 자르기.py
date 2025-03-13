n,m = map(int,input().split())
array = list(map(int,input().split()))
result = []

def binary_search(array,start,end,target):
    if start > end:
        return
        
    mid = (start + end) // 2
    
    if calc(array,mid) >= target:
        result.append(mid)
        binary_search(array,mid+1,end,target)
    else:
        binary_search(array,start,mid-1,target)

def calc(array,mid):
    result = 0
    for i in array:
        if i >= mid:
            result += (i - mid)
    return result
    
binary_search(array,0,max(array),m)
print(max(result))