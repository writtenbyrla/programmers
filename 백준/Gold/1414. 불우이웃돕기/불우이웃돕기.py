def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x,y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x == root_y:
        return
    parent[root_x] =root_y

n = int(input())
length = [list(input().rstrip()) for _ in range(n)]
parent = [i for i in range(n+1)]
graph = []
total = 0

for i in range(n):
    for j in range(n):
        # 랜선 길이 계산
        # 소문자 알파벳의 경우
        if 'a' <= length[i][j] <= 'z':
            k = ord(length[i][j]) - ord('a') + 1
            graph.append((k, i, j))
            total += k

        # 대문자 알파벳의 경우
        elif 'A' <=  length[i][j]  <= 'Z':
            k = ord(length[i][j]) - ord('A') + 27
            graph.append((k, i, j))
            total += k

graph.sort()
result = 0
used_edges = 0

for edge in graph:
    cost, start, end = edge
    if find(parent,  start) != find(parent, end):
        union(parent, start, end)
        result += cost
        used_edges += 1
        if used_edges == n-1:
            break

if used_edges == n-1:
    print(total - result)
else:
    print(-1)