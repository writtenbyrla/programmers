n = int(input())
arr = list(map(int, input().split()))
delete = int(input())


# 노드 삭제 시 -2로 변경
# dfs로 노드값이 -2인 경우 부모 노드를 다시 값 넘김
def dfs(num):
    arr[num] = -2
    for i in range(n):
        if num == arr[i]:
            dfs(i)

dfs(delete)
count = 0

for i in range(n):
    if arr[i] != -2 and i not in arr:
        count+=1

print(count)