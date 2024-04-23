# arr 길이가 홀수라면 짝수 인덱스 위치에 n을 더한 배열
# arr 길이가 짝수라면 홀수 인덱스 위치에 n을 더한 배열 리턴

# 1. n이 홀수일 때, 짝수일 때 조건문 나눔
# 2. n을 더한다(홀수일 경우 짝수인덱스, 짝수일 경우 홀수인덱스에 n 더함) -> 2씩 건너뜀
def solution(arr, n):
    
    if (len(arr) %2 == 0):
        for i in range(1, len(arr), 2):
            arr[i] += n
    else:
        for i in range(0, len(arr), 2):
            arr[i] += n
    
    return arr