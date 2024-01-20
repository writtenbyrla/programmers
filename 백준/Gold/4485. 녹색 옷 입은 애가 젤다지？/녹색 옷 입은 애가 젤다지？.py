import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
def cave(graph):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    rupee = [[INF] * N for _ in range(N)]

    q=[]
    rupee[0][0] = graph[0][0]
    heapq.heappush(q, (graph[0][0], 0 ,0))

    while q:
        acc, x, y = heapq.heappop(q)

        if rupee[x][y] < acc:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(graph) and 0<=ny<len(graph):
                rupee_sum = rupee[x][y] + graph[nx][ny]
                if rupee_sum < rupee[nx][ny]:
                    rupee[nx][ny] = rupee_sum
                    heapq.heappush(q, (rupee_sum, nx, ny))
    return rupee[-1][-1]

count = 0 # 테스트 횟수 카운팅
while True:
    N = int(input().strip())

    if N == 0:
        break

    count +=1
    graph = [list(map(int, input().split())) for _ in range(N)]
    print(f"Problem {count}: {cave(graph)}")