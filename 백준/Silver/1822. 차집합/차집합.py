import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

# 방법1) A 순회하면서 B와 일치하는 값 있으면 제거
# -> 이중 for문 + 값 저장할 별도 자료구조 필요
# 방법2) set 집합 A-B

print(len(a-b))
print(*sorted(list(a-b)))