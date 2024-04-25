def solution(num_list):
    a=""
    b=""
    for num in num_list:
        if num % 2:
            a += str(num)
        else:
            b += str(num)
    return int(a)+int(b)