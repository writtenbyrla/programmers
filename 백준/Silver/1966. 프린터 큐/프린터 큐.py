from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    imp = deque(map(int, input().split()))
    idx= deque(list(range(N)))

    cnt = 0

    while imp:
        if imp[0]==max(imp):
            cnt+=1
            imp.popleft()
            if idx.popleft() == M: 
                print(cnt) 
        else:
            imp.append(imp.popleft())
            idx.append(idx.popleft())