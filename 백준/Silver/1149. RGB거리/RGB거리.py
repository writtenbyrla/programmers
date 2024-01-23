import sys
input = sys.stdin.readline

N = int(input())
home = [[]*N for _ in range(N)]
for i in range(N):
    home[i] = list(map(int, input().split()))

dp = [[0]*3 for _ in range(N)]
dp[0] = home[0]

for i in range(1, N):
    # 이전 줄의 겹치지 않는 색깔 중 최솟값과 더해서 dp에 담음
    dp[i][0] = home[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = home[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = home[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1])) #누적된 값 중 가장 작은 값