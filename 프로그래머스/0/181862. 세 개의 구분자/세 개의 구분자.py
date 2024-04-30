def solution(myStr):
    answer = []
    for char in myStr:
        if char in ['a', 'b', 'c']:
            myStr = myStr.replace(char, ' ')
    answer = myStr.split()
    return answer if answer else ["EMPTY"]