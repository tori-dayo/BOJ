def solution(s):
    cnt = 0
    total_cnt = 0
    
    while True:
        if len(s) == 1:
            break
        # 0의 개수를 센 후, 토탈에 더해준다.
        zero_cnt = s.count('0')
        total_cnt += zero_cnt
        # 0을 제거한 후의 길이를 잰다.
        s = s.replace('0','')
        s_len = len(s)
        # s를 다시 갱신해준다.
        s = bin(s_len)
        s = s[2:]
        cnt += 1
    result = [cnt,total_cnt]
    return result