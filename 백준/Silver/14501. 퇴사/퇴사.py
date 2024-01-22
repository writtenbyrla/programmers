import sys
input = sys.stdin.readline

N = int(input())
table = [tuple(map(int, input().split())) for _ in range(N)]

max_val = 0

# dp(n번째 날, 여태까지 번 돈)
# -> 근무를 한다면 dp(n+t, 여태까지 번 돈 + n번째날에 번 돈)
# -> 근무를 안한다면 dp(n+1, 여태까지 번 돈)
def dp(idx, pay):
    global max_val
    if idx >= N:
        if pay > max_val:
            max_val = pay
        return

    t, p = table[idx]

    for i in range(2):
        if i==1:  # 근무하는 경우
            if idx+t > N:
                return
            dp(idx+t, pay+p)
        else:
            dp(idx+1, pay)
dp(0,0)
print(max_val)
