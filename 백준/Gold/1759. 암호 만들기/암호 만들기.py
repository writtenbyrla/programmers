l, c = map(int, input().strip().split())
arr = list(map(str, input().split()))
arr.sort()
vowel = ['a','e','i','o','u']
result = []
def dfs(start, current, v, c):
    # 길이 l일때 모음 1, 자음 2
    if len(current) == l:
        if 1 <= v and 2<= c:
            result.append(''.join(current))
        return

    for i in range(start, len(arr)):
        if arr[i] in vowel:
            current.append(arr[i])
            dfs(i+1, current, v+1, c)
            current.pop()
        else:
            current.append(arr[i])
            dfs(i+1, current, v, c+1)
            current.pop()

dfs(0, [], 0, 0)

for char in result:
    print(char)