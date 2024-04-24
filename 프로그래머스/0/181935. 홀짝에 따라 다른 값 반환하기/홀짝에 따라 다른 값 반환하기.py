# n이 홀수 -> n이하의 모든 홀수 더하기
# n이 짝수 -> n이하의 짝수 제곱 합
def solution(n):
    answer = 0
    if n%2==1:
        for num in range(1,n+1,2):
            answer += num
    else: 
        for num in range(2, n+1, 2):
            answer += num*num
    return answer