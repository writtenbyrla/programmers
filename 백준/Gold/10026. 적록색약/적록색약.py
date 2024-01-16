import sys
sys.setrecursionlimit(10000)
n = int(sys.stdin.readline())

array = [[]*n for _ in range(n)]
for i in range(n):
    array[i] = list(sys.stdin.readline().strip())

cnt = 0
visited = [[False]*n for _ in range(n)]
def bfs(a,b,eyes,color):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if x < 0 or x >= n or y < 0 or y >=n or visited[x][y]:
            continue

        if(eyes == 'color-blindness'):
            if((color != 'B') and array[x][y] != 'B'):
                visited[x][y] = True
                bfs(x, y, eyes, color)
            elif(color == 'B' and array[x][y] =='B'):
                visited[x][y] = True
                bfs(x, y, eyes, color)
            else:
                continue


        else:
            if color == array[x][y]:
                visited[x][y] = True
                bfs(x,y,eyes,color)

    return

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,'!color-blindness',array[i][j])
            cnt += 1

print(cnt,end=' ')
visited= [[False]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j] :
            bfs(i,j,'color-blindness',array[i][j])
            cnt += 1
print(cnt)