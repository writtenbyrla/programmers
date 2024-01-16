import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y, color, isblind):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            # 적록색약일 경우
            if isblind == 'blind':
                if color != 'B' and arr[nx][ny] != 'B':
                    visited[nx][ny] = True
                    dfs(nx, ny, color, isblind)
                elif color == 'B' and arr[nx][ny] == 'B':
                    visited[nx][ny] = True
                    dfs(nx, ny, color, isblind)
                else:
                    continue

            # 적록색약 아닐 경우
            else:
                if color == arr[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny, color, isblind)
    return


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
visited = [[False] * n for _ in range(n)]
arr = [list(input().rstrip()) for _ in range(n)]

count = 0
blind_count = 0

# 적록색약 아닐 경우
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, arr[i][j], '!blind')
            count += 1

# 적록 색약일 경우
# visitied 배열 초기화
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, arr[i][j], 'blind')
            blind_count +=1

print(count, blind_count)