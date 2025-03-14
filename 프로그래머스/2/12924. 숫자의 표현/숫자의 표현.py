def solution(n):
    cnt = 1
    
    for i in range(1,n):
        result = i
        for j in range(i+1,n):
            result += j
            if result == n:
                cnt += 1
                break
            elif result > n:
                break
    return cnt