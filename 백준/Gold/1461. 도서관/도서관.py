import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))

# 양수, 음수 나누기
positive = []
negative = []

for book in books:
    if book > 0 :
        positive.append(book)
    else:
        negative.append(abs(book))

positive.sort(reverse=True)
negative.sort(reverse=True)

dist = []
# 인덱스가 M으로 나누어지는 경우 = M권 단위로 이동 가능
# dist 배열에 담음
for i in range(len(positive)):
    if i % M == 0:
        dist.append(positive[i])
for i in range(len(negative)):
    if i % M == 0:
        dist.append(negative[i])

dist.sort()
# 책 갖다놓고 돌아와야해서 *2 / 마지막에는 안돌아와도 되니까 안더해줌
step = 2 * sum(dist) - dist[-1]
print(step)