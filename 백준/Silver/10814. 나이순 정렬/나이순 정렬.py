import sys
input = sys.stdin.readline

n = int(input())

users = []
for index in range(n):
    age, name = map(str, input().split())
    users.append([index, int(age), name])

users.sort(key=lambda x:(x[1], x[0]))

for index, age, name in users:
    print(age, name)