import heapq
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    answer = 0
    for _ in range(k-1):
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        answer += a+b
        heapq.heappush(files, a+b)
    print(answer)