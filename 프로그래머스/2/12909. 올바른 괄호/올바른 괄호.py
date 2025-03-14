def solution(s):
    cnt = 0
    
    for i in range(0,len(s)):
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            if cnt == 0:
                return False
            else:
                cnt -= 1
    
    if cnt == 0:
        return True
    else:
        return False
    
    