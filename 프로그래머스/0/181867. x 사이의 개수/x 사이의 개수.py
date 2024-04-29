def solution(myString):
    answer = []
    answer2 = []
    answer = myString.split('x')
    for char in answer:
        answer2.append(len(char))
    return answer2