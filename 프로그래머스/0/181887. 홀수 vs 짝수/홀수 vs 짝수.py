def solution(num_list):
    if sum(num_list[0::2]) < sum(num_list[1::2]):
        return sum(num_list[1::2])
    else:
        return sum(num_list[0::2])
