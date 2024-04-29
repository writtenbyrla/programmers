def solution(arr, delete_list):
    # for num in delete_list:
    #     if num in arr:
    #         arr.remove(num)
    # return arr

    return [i for i in arr if i not in delete_list]