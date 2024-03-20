def solution(brown, yellow):
    # 카펫의 가로, 세로 크기
    # brown = (y_width*2)+(y_height*2)+4
    
    answer = []
    
    y_width = 0
    y_height = 0
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            y_width = int(yellow/i)
            y_height = i
            if (y_width*2)+(y_height*2)+4 == brown:
                answer.append(y_width+2)
                answer.append(y_height+2)
                
                return sorted(answer, reverse = True)
    
    return answer