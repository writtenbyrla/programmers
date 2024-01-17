import sys
input = sys.stdin.readline

#전화번호 목록이 일관성을 유지하려면,
# 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.

t = int(input()) # 테스트케이스 수

for _ in range(t):
    n = int(input())  # 전화번호 수
    nums = [input().strip() for _ in range(n)] # 전화번호 리스트
    nums.sort()

    isConsis = True
    # 현재 번호가 다른 번호에서 그 길이만큼 일치하는지 확인
    for i in range(n-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            isConsis = False
            break

    if not isConsis:
        print('NO')
    else:
        print('YES')