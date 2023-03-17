import sys

from collections import defaultdict

def dfs(x, y):
    
    if x == M - 1 and y == N - 1: #목적지에 도착했을 때 1을 리턴하여 더한다.
        return 1
    
    if dp[x][y] != -1: # 이미 탐색하였다면 
        return dp[x][y]
        
    dp[x][y] = 0
    
    for i in range(4):
        new_x = x + direction[i][0]
        new_y = y + direction[i][1]
        
        if 0 <= new_x < M and 0 <= new_y < N:
                if graph[x][y] > graph[new_x][new_y]:
                    dp[x][y] += dfs(new_x, new_y) 
    return dp[x][y]

if __name__ == "__main__":
    input = sys.stdin.readline

    M, N = map(int, input().split()) # M: 세로크기, N: 가로크기

    graph =  [list(map(int, input().split())) for _ in range(M)]

    dp = [[-1 for _ in range(N)] for _ in range(M)]
        
    direction = [(-1,0), (1,0), (0, -1), (0, 1)] #상 하 좌 우    
            
    print(dfs(0,0))                          
