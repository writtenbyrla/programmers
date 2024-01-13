class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        # 더 이상 부모 노드가 없을대 x 자체 리턴
        if self.parent[x] == x:
            return x
        # 더 이상 부모 노드가 없을때까지 재귀적으로 부모노드 찾음
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        # 두 노드의 부모 노드가 다른 경우 연결
        self.parent[root_x] = root_y

if __name__ == '__main__':
    from sys import stdin, setrecursionlimit
    input = stdin.readline
    setrecursionlimit(10 ** 5)

    n, m = map(int, input().split()) # 집 수, 다리 수
    s, e = map(int, input().split()) # 숭이집, 혜빈이집

    bridge = []

    for _ in range(m):
        x, y, k = map(int, input().split())
        bridge.append((k, x, y)) #다리 무게 제한, 노드1, 노드2

    bridge.sort() # 가중치가 높은 순으로 오름차순 정렬

    djs = DisjointSet(n)
    
    last = 0 # 마지막으로 사용한 간선의 가중치
    
    while djs.find(s) != djs.find(e) and bridge: # 아직 연결 X, 다리가 남아있을 때 동안
        d, x, y = bridge.pop() #가중치가 높은 간선부터
        last = d # 가중치 갱신
        djs.union(x, y) # 두 노드 연결

    # 시작과 끝 노드가 이어졌을때 가중치 출력
    # 연결이 안 된 경우 0 출력
    
    print(last if djs.find(s) == djs.find(e) else 0)