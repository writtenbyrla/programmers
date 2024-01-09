import heapq
# 카드 합체 놀이
# n: 카드 개수, m=합체 횟수
n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

# 힙 정렬시 최소힙이 되므로 가장 작은 수 heappop 연산으로 뽑기
heapq.heapify(cards)
for i in range(m):
    # 제일 작은 수 두개 뽑아내기
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    
    # 더한 값을 다시 힙에 넣기(덮어쓰기)
    heapq.heappush(cards, x+y)
    heapq.heappush(cards, x+y)

print(sum(cards))