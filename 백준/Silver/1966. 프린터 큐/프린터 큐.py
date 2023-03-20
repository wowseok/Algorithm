import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split()) #N:문서의 개수, M: M번째 인덱스가 몇번째 순서로 출력되는지
    dq = deque(list(map(int, input().split())))
    index = deque(list(range(N)))
    
    cnt = 0
    
    while dq:
        if dq[0] == max(dq): # 맨 앞에있는값이 제일 크면
            cnt +=1
            dq.popleft()
            pop_index = index.popleft() #인덱스를 따로 관리
            if pop_index == M:          # 계속 pop할동안 M번째 인덱스와 같아지면 cnt 출력 
                print(cnt)
        
        else:
            dq.append(dq.popleft()) #맨 앞 값이 max가 될때까지 pop한 후 append 
            index.append(index.popleft())