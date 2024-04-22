def solution(num_list):
    num_list.sort()
    return num_list[-(len(num_list)-5):]