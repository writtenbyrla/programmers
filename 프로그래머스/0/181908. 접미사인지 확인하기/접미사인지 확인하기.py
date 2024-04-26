def solution(my_string, is_suffix):
    # is_suffix의 길이를 구해서 my_string 뒤에서 그 길이만큼 추출해서 일치여부 확인하기
    return 1 if my_string[-len(is_suffix):] == is_suffix else 0