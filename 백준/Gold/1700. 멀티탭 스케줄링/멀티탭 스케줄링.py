n, k = map(int, input().split())
array = list(map(int, input().split()))
result = []
cnt = 0

for i in range(k):
    x = array[i]

    # 이미 꽂혀 있으면 패스
    if x in result:
        continue

    # 빈 자리 있으면 그냥 꽂기
    if len(result) < n:
        result.append(x)
        continue

    # 교체할 전기기구 찾기
    max_idx = -1
    idx = -1

    for j in range(n):
        if result[j] not in array[i+1:]:  # 앞으로 안 쓰일 기구 찾으면 바로 제거
            idx = j
            break

        # enumerate로 가장 나중에 나오는 기구 찾기
        for pos, val in enumerate(array[i+1:], start=i+1):
            if val == result[j]:
                if pos > max_idx:
                    max_idx = pos
                    idx = j
                break

    # 가장 나중에 등장할 기구를 제거하고 새 기구 꽂기
    result[idx] = x
    cnt += 1

print(cnt)