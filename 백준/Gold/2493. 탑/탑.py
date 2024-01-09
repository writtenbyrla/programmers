n = int(input())
top = list(map(int, input().split()))
top_list = [(num, i) for i, num in enumerate(top)]
result = [0] * n
stack = []

# 왼쪽 방향으로 순회(역순으로 for문)
for num, i in top_list[::-1]:
    # 현재 확인할 탑
    current_top = top_list[i]
    index = current_top[1]
    
    # 스택에 담긴 값보다 크면 현재 탑에서 이전 탑의 신호를 수신하니까
    # 이전 탑의 result에 현재 탑의 index+1이 담겨야 함(index는 0부터 시작이므로)
    while stack and stack[-1][0] < current_top[0]:
        prev = stack.pop()
        result[prev[1]] = index + 1
    stack.append(current_top)
    
print(*result)