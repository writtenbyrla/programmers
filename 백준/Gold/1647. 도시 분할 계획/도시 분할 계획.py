def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        parent[root_y] = root_x

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

result = 0
max_cost = 0

for edge in graph:
    cost, start, end = edge
    if find(parent, start) != find(parent, end):  # 연결이 안됐을 경우
        union(parent, start, end)  # 연결해서
        result += cost  # 비용을 더해줌
        max_cost = max(cost, max_cost)  # 가장 큰 값

print(result - max_cost)  # 가장 큰 간선 제외