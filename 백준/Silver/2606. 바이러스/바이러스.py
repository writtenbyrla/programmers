import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터 대수
m = int(input()) # 연결선 개수

# 방문한 컴퓨터인지 확인하는 visited, 연결된 컴퓨터 목록인 graph 생성
# 인덱스를 1로 맞추기 위해 둘 다 n+1개만큼
visited = [0]*(n+1)
graph = [[] for i in range(n+1)]

# 연결선 개수만큼 두 노드를 서로 연결
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    stack = [start]
    while stack:
        current_com = stack.pop()
        if not visited[current_com]:
            visited[current_com] = 1
            global count
            count += 1
            for adj in graph[current_com]:
                if adj not in visited:
                    stack.append(adj)

count = 0
dfs(1)

print(count-1)