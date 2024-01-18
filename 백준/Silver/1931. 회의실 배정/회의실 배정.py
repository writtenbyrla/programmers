import sys
input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))
answer = 0
cur = 0
for start, end in meetings:
    if cur<= start:
        answer +=1
        cur = end
print(answer)