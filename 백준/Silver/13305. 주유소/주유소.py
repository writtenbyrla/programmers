import sys
input = sys.stdin.readline

# 첫 번째 도시에서 무조건 주유
# 현재까지 이동한 거리가 다음 주유소까지 거리 이상이면 다음 주유소로 이동
# 이동한 거리가 더 적을 경우 기름 충전

n = int(input()) # 도시 수
distance = list(map(int, input().split())) # 도로 길이(n-1)
cost = list(map(int, input().split())) # 주유소 리터당 가격(n개)

total = 0

min_cost = cost[0]
for i in range(n-1):
    if min_cost > cost[i]: # 현재 주유소가 최저가보다 더 싼 경우
        min_cost = cost[i] # 최저가 갱신 후
    total += min_cost * distance[i] # 가장 싼 주유소에서 충전
print(total)