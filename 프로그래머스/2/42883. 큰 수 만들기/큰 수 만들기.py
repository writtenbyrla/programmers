def solution(number, k):
    # number 각 요소를 스택에 넣음
    # k개 만큼 제거 후 반환
    
    stack = []
    
    for num in number: 
        # 현재 수와 스택에 담긴 수 비교
        # 현재수가 더 크면 스택에 있는 수 제거 후 num 담음
        while stack and stack[-1] < num and k>0:
            stack.pop()
            k -= 1
        stack.append(num) 
    
    if k>0:
        stack = stack[:-k]
    
    return ''.join(stack)