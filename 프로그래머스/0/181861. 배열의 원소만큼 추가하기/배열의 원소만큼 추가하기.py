def solution(arr):
    answer = []
    for num in arr:
        for i in range(0, num):
            answer.append(num)    
    return answer