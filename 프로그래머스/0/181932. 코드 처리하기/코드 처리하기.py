def solution(code):
    answer = ''
    mode = 0
    
    for idx in range(0, len(code)):
        if mode == 0:
            if code[idx]!='1' and idx%2==0:
                answer+=code[idx]
            elif code[idx]=='1':
                mode = 1
        elif mode == 1:
            if code[idx]!='1' and idx%2==1:
                answer += code[idx]
            elif code[idx]=='1':
                mode = 0
    return answer if answer else "EMPTY"    