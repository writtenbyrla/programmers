import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

lo, hi = 1, max(trees)
result = 0
while lo <= hi:
    mid = (lo + hi) // 2
    height = 0
    for tree in trees:
        if tree > mid:
            height += (tree - mid)

    if height >= m:
        result = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(result)