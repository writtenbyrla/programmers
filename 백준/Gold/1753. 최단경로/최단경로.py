import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        acc, cur = heapq.heappop(q)

        if dist[cur] < acc:
            continue

        for adj, w in graph[cur]: 
            sum_w = acc + w
            if sum_w < dist[adj]:
                dist[adj] = sum_w
                heapq.heappush(q, (sum_w, adj))

# 입력 받는 부분
V, E = map(int, input().split()) # 노드, 간선 수
k = int(input()) # 시작 노드 번호
dist = [INF] * (V + 1)

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(k)
for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else: 
        print(dist[i])