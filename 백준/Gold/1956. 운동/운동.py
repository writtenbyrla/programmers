import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split()) # 마을 수(1~), 도로 수
dist = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c

# 최단 경로 구하기
for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            if dist[a][k] + dist[k][b] < dist[a][b]:
                dist[a][b] = dist[a][k] + dist[k][b]

min_cycle = INF
for i in range(1, V+1):
        min_cycle = min(min_cycle, dist[i][i])

if min_cycle == INF:
    print(-1)
else:
    print(min_cycle)