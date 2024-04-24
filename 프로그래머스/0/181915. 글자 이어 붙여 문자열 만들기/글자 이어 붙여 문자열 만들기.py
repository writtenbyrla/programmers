def solution(my_string, index_list):
    answer = ''
    for num in index_list:
        answer += my_string[num]
    return answer