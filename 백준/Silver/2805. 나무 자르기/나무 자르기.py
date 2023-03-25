import sys

input = sys.stdin.readline

N, M = map(int, input().split()) #나무의 수, 나무의 길이
tree_height = list(map(int, input().split()))


start, end = 0, max(tree_height)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(N):
        if tree_height[i] < mid: # 절단기 높이보다 낮은 나무는 자를 수 없다.
            pass
        else:
            cnt += tree_height[i] - mid
    
    if cnt >=M: #자른 나무의 길이가 가져가려고하는 나무의 길이 M보다 크다면
        start = mid + 1 # 더 많이 잘라야한다. (start의 범위를 조정하면 다음 while문에서 (start + end // 2)일 때 더 높은 위치로 절단함.
    
    else:
        end = mid - 1 # 더 적게 잘라야한다.

#print(cnt)
print(end)
        
        
