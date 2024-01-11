T = int(input()) # 테스트 수
def dfs(n, sum):
    global count

    # 탐색 종료 조건
    if sum == n:
        count += 1
        return

    elif sum > n:
        return

    for i in range(1, 4):
        if sum + i <= n:
            dfs(n, sum+i)

for _ in range(T):
    n = int(input()) # 정수 n
    count = 0
    dfs(n, 0)
    print(count)