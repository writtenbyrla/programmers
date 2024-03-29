import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
answer = 0
for i in range(n-1, -1, -1):
    answer += k//coins[i]
    k %= coins[i]
print(answer)