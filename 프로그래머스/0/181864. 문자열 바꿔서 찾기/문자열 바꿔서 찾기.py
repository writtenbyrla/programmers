def solution(myString, pat):
    newString = '';
    for char in myString:
        if char == 'A':
            newString+='B'
        else:
            newString+='A'
    
    return 1 if pat in newString else 0