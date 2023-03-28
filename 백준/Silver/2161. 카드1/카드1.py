import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque(i for i in range(1,N+1))
answer = []

while dq:
    answer.append(dq.popleft())
    
    if dq:
        dq.append(dq.popleft())

print(" ".join(map(str, answer)))

    
