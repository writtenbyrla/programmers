import sys
input = sys.stdin.readline

def find(parent, x):
    # 더 이상 부모 노드가 없을대 x 자체 리턴
    if parent[x] == x:
        return x
    # 더 이상 부모 노드가 없을때까지 재귀적으로 부모노드 찾음
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    # root_y가 더 큰 경우 root_y의 부모를 root_x로 합침
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

n = int(input()) #행성 수
cost_arr = [list(map(int,input().split())) for _ in range(n)] # 행성간 관리 비용
parent = [i for i in range(n)] #부모노드 1~n 세팅

edges = []
for i in range(1, n):
    for j in range(i):
        edges.append((cost_arr[i][j], i, j))
edges.sort() # 최소 비용순으로 확인

answer = 0
for cost, x, y in edges:
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        answer += cost
print(answer)