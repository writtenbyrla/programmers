import sys
input = sys.stdin.readline

# 서류, 면접순위 튜플로 묶어서 서류 순으로 오름차순 정렬
# 면접순위 비교해서 선발여부 결정

t = int(input())

for _ in range(t):
    answer = 0
    n = int(input())
    # 서류 순위, 면접 순위(숫자가 낮을수록 좋음)
    applicants = [tuple(map(int,input().split())) for _ in range(n)]
    applicants = sorted(applicants, key=lambda x:(x[0]))

    selected = 1 # 서류 1등은 항상 선발
    interview_rank = applicants[0][1] # 서류 1등 면접 등수

    for i in range(1, n):
        if applicants[i][1] < interview_rank: # 앞 사람보다 면접 등수가 더 높을경우 선발
            selected += 1
            interview_rank = applicants[i][1] # 현재 확인한 지원자 면접등수로 다음 지원자 비교

    print(selected)