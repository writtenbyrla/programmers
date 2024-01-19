import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())
budgets.sort()

# end를 상한선으로 잡음
start, end = 0, max(budgets)

while start <= end:
    mid = (start + end) // 2
    # 전체 예산 = 상한선과 요청액 비교해서 상한선보다 클 경우 상한선으로 더함
    budgets_sum = sum(min(mid, request) for request in budgets)

    # 총 예산보다 클 경우 상한선을 낮춤
    if budgets_sum > m:
        end = mid - 1
    # 총 예산보다 작을 경우 상한선 높임
    else:
        start = mid + 1
print(end)