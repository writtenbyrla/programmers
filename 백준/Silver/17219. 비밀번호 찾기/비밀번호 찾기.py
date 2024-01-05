N, M = map(int, input().split())
table = {}

for i in range(N):
    site, pw = map(str, input().split())
    table[site] = pw

for _ in range(M):
    site = str(input().strip())
    print(table[site])