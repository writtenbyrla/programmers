import sys
input = sys.stdin.readline

n = int(input())
count = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

home = []

# n * n 배열
for _ in range(n):
    row = list(map(int, input().strip()))
    home.append(row)

result = []

def dfs(x, y):
    global count
    stack = [(x, y)]
    home[x][y] = 0  # 한번 방문한 곳은 다음 탐색때 통과하도록 0으로 다시 바꿔줌
    count = 1

    while stack:
        x, y = stack.pop()

        for i in range(4): # 인접한 노드 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 인접한 곳이 1일때(집이 있을때 = 같은 단지일때)
            if 0 <= nx < n and 0 <= ny < n and home[nx][ny] == 1:
                stack.append((nx, ny))
                home[nx][ny] = 0  # 방문한 곳은 0으로 변경
                count += 1

for row in range(n):
    for col in range(n):
        if home[row][col] == 1:
            dfs(row, col)
            result.append(count)

result.sort()
print(len(result))
for cnt in result:
    print(cnt)