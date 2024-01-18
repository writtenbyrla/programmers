import sys
input = sys.stdin.readline

n = int(input())
takeout = list(map(int, input().split()))
takeout.sort()
answer = 0
answerlst = []
for i in range(n):
    answer += takeout[i]
    answerlst.append(answer)
print(sum(answerlst))