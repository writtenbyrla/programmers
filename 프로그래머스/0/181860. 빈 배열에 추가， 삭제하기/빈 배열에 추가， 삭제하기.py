def solution(arr, flag):
    answer = []
    for i, b in enumerate(flag):
        if b:
            for j in range(0, arr[i]*2):
                answer.append(arr[i])
        else:
            for j in range(0, arr[i]):
                answer.pop()
    return answer