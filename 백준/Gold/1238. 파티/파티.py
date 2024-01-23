import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline
INF = int(1e9)

def party(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        acc, cur = heapq.heappop(q)
        if dist[cur] < acc:
            continue
        for adj, time in road[cur]:
            sum_time = acc + time
            if sum_time < dist[adj]:
                dist[adj] = sum_time
                heapq.heappush(q, (sum_time, adj))

    return dist

# 가장 많은 시간 소비한 학생의 소요시간
# 학생수, 도로수, 마을
N, M, X = map(int, input().split())

road = defaultdict(list)
for _ in range(M):
    # 도로 시작점, 끝점, 소요시간
    start, end, time = map(int, input().split())
    road[start].append((end, time))

result = [0] * (N+1)
for i in range(1, N+1):
    dist = [INF] * (N + 1)
    result[i] = party(i)

max_time = 0
for i in range(1, N + 1):
    max_time = max(max_time, result[i][X] + result[X][i])

print(max_time)