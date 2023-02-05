import sys

while(True):
    total_max = 0
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break  
    else:
        arr = []
        for i in range(N):
            arr.append(list(map(int, sys.stdin.readline().split())))
        max_list = max(arr) # 2차원 배열범위에서 1차원 배열 배열 범위의 최대값
        total_max = max(max_list) #1이 있는지 체크
        if N == 1 or M == 1:
            print(total_max)
            continue
        for i in range(1, N):
            for j in range(1, M):
                if ( arr[i][j] != 0):
                    arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1])+1
                    if total_max < arr[i][j]:
                        total_max = arr[i][j]
    print(total_max)
