from collections import deque

# 노드 수, 간선 개수, 탐색 시작 번호
n, m, v = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

# 연결선 개수만큼 두 노드 연결
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for num in graph:
    num.sort()

# dfs 방식
def dfs(start, visited):
    visited.append(start)

    for adj in graph[start]:
        if adj not in visited:
            dfs(adj, visited)

    return visited

# bfs 방식
def bfs(start):
    visited = [start]
    q = deque([start])
    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)
    return visited

print(" ".join(map(str, dfs(v, []))))
print(" ".join(map(str, bfs(v))))