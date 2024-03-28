import sys
from collections import deque
input = sys.stdin.readline

# 안전한 영역의 최대 개수
# 아무 지역도 물에 잠기지 않을 수도 있다. -> 비오는 양 최대 높이 99
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, height, visited):
    q = deque([(x,y)])
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] > height:
                visited[nx][ny] = 1
                q.append((nx, ny))



n = int(input())
answer = 0
area = []

for _ in range(n):
    height = list(map(int, input().split()))
    area.append(height)

safe_zone = 0
for height in range(100):
    visited = [[0]*n for _ in range(n)]
    count = 0
    # visited가 0, home[i][j]>높이 일 때 그래프 탐색 후 count+1
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0 and area[i][j]>height:
                bfs(i, j, height, visited)
                count +=1
    safe_zone = max(safe_zone, count)

print(safe_zone)