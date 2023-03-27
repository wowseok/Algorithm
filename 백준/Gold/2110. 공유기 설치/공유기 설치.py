import sys

input = sys.stdin.readline

N, C = map(int, input().split()) # N: 집의 개수, C: 공유기의 개수

arr = []
for i in range(N):
    arr.append(int(input()))
    
arr.sort()

start = 1 #최소거리
end = arr[-1] - arr[0] #최대거리
answer = 0

while start <= end:
    mid = (start + end) // 2 #최소거리와 최대거리의 중앙
    cnt = 1
    current = arr[0] # 앞집부터 설치
    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            cnt += 1
            current = arr[i]
    
    if cnt >= C: #공유기를 좁게 설치했으므로 더 넓게 설치할 수 있다.
            start = mid + 1
            answer = mid
    else:
        end = mid - 1
print(answer)
            
            