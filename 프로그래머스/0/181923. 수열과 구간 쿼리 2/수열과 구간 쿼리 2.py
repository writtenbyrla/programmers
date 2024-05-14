def solution(arr, queries):
    answer = []
    
    # queries 순회하는 반복문
    # queries[i][0] ~ queries[i][1]을 만족하는 arr 요소를 subarr에 담기
    # queries[i][2]보다 큰 arr 요소 answer에 담기
    # 더 큰 값이 없는 경우(subarr 순회 끝나면 답이 없으므로 -1 담기)
    
    for query in queries:
        subarr = arr[query[0]:query[1]+1]
        subarr.sort()
        for num in subarr:
            if num > query[2]:
                answer.append(num)
                break
            elif num == subarr[-1]:
                answer.append(-1)
    return answer