def solution(arr, queries):
    # queries 배열 순차적으로 순회하면서
    # 각 쿼리에 따라 arr 자리 뒤바꿈 
    
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
    
    return arr