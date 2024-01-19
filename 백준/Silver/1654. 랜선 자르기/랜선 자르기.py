import sys
input = sys.stdin.readline

k, n = map(int, input().split()) # 랜선 개수, 필요한 랜선 개수
lines = list(int(input()) for _ in range(k)) # 각 랜선의 길이

lo, hi = 1, max(lines)
result = 0
while lo <= hi:
    mid = (lo + hi) // 2 # 기준값
    line_sum = 0
    # 기준값으로 잘랐을때 랜선 몇개 나오는지 계산
    for line in lines:
        line_sum += line // mid

    if line_sum >=n:
        result = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(result)