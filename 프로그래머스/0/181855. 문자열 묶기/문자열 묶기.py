def solution(strArr):
    dict = {}
    for string in strArr:
        if len(string) in dict: 
            dict[len(string)] += 1
        else:
            dict[len(string)] = 1
    return max(dict.values())