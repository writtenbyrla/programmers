def solution(n):
    # number = str(n)
    # answer = 0
    # for num in number:
    #     answer += int(num)
    # return answer
    
    return sum(int(i) for i in str(n))