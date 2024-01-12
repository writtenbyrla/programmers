from collections import deque
import sys; input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

# 연결 트리
tree = dict()
for i in range(1, n+1):
    tree[i] = []

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque([1])
# 부모노드 0으로 세팅
parent = [0] * (n+1)

while q:
    current = q.popleft()
    for i in tree[current]:
        # 부모노드가 설정 X and 루트노드 제외
        if parent[i] == 0 and i!=1: # 루트 노드 제외
            parent[i] = current
            q.append(i)

for i in range(2, n+1):
    print(parent[i])