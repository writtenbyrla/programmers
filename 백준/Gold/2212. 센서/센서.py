import sys
input = sys.stdin.readline

# 최대 k개의 집중국의 수신 가능 영역 길이의 합의 최솟값
# 인접한 두 센서의 차이
# 센서를 묶어 집중국을 k개로 나눔

n = int(input()) # 센서 개수
k = int(input()) # 집중국 개수
sensors = list(map(int, input().split())) # 센서 좌표
sensors.sort() # 가까운 순으로 정렬 1, 3 // 6, 6, 7, 9 => 2, 3
distance = []

for i in range(0, n-1):
    distance.append(sensors[i+1] - sensors[i])

distance.sort()
print(sum(distance[:n-k]))