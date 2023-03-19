import sys

input = sys.stdin.readline
K, N = map(int, input().split())

lan = [int(input()) for _ in range(K)]


start, end = 1, max(lan)

while start <= end: 
    mid = (start + end) // 2
    cnt = 0 
    for i in range(K):
        cnt += lan[i] // mid
        
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)