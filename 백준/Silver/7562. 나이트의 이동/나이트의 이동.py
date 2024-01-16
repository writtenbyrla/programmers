import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
def bfs(x, y, x2, y2, visited):
    q = deque()
    q.append((x,y))

    while q:
        currentX, currentY = q.popleft()
        if currentX == x2 and currentY == y2:
            print(visited[currentX][currentY] -1)
            return

        for i in range(8):
            nx = currentX + dx[i]
            ny = currentY + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[currentX][currentY] + 1
                q.append((nx, ny))
    return False


n = int(input())

for i in range(n):
    l = int(input())    # 체스판 크기
    x, y = map(int, input().split()) # 현재 위치 좌표
    x2, y2 = map(int, input().split()) # 옮겨갈 위치 좌표
    visited = [[0]*l for _ in range(l)] # 방문표시 0으로 세팅
    visited[x][y] = 1
    bfs(x, y, x2, y2, visited)