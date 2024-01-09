# 차의 대수
n = int(input())
input_list = {}
output_list = []

# 입구에서 들어가는 순서로 딕셔너리를 만듦
for i in range(n):
    car_number = str(input()).strip()
    input_list[car_number] = i

# 출구에서 나오는 순서대로 리스트에 저장
for i in range(n):
    output_list.append(str(input()).strip())

# 추월한 차량 수
count = 0
# 나온 순서대로 하나씩 그 다음에 나온 차보다 먼저 나왔는지 비교
for i in range(n-1):
    for j in range(i+1, n):
        if input_list[output_list[i]] > input_list[output_list[j]]:
            count += 1
            break
print(count)