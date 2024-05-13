def solution(a, d, included):
    answer = 0
    arr=[]
    for i in range(len(included)):
        arr.append(a+(d*i))
    
        if included[i]:
            answer += arr[i]
        
    return answer