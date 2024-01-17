from collections import Counter
import sys
input = sys.stdin.readline

# 출력값
# 평균, 중앙값, 최빈값(중복 시 두 번째로 작은 값), 범위(최댓값과 최솟값의 차이)

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

# 평균
print(round(sum(nums)/n))

# 중앙값
index = n // 2
print(nums[index])

# 최빈값
counter = Counter(nums) # Counter({-2: 1, 1: 1, 2: 1, 3: 1, 8: 1})
# 튜플의 두번째 요소 기준 내림차순 정렬, 요소가 같을 경우 오름차순 정렬
counter_lst = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

if len(counter_lst) > 1:
    if counter_lst[0][1] == counter_lst[1][1]:
        print(counter_lst[1][0])
    else:
        print(counter_lst[0][0])
else:
    print(counter_lst[0][0])
    
# 범위
print(nums[-1] - nums[0])