import heapq
import sys
input = sys.stdin.readline

# 종료시간 순으로 비교
# heap에 종료시간을 담아
# 1. 새 강의의 시작시간이 빠르면 새 강의의 종료시간도 담음
# 2. 새 강의의 시작시간이 heap에 담긴 종료시간보다 같거나 크면 기존 종료시간 제거, 새 강의의 종료시간 삽입
# 힙 길이의 수 = 강의실 개수

n = int(input())
classes = [tuple(map(int, input().split())) for _ in range(n)]
classes.sort(key=lambda x: x[0]) # 시작 시간 기준 정렬

heap = []
heapq.heappush(heap, classes[0][1])

for i in range(1, n):
    if classes[i][0] < heap[0]:
        heapq.heappush(heap, classes[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, classes[i][1])

print(len(heap))