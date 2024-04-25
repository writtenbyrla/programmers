def solution(num_list):
    answer = 0
    multiply = 1
    for num in num_list:
        multiply *= num
    if multiply <sum(num_list)**2:
        return 1
    return answer