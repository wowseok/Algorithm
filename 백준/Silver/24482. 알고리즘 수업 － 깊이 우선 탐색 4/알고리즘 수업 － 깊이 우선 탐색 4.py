import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드
input = sys.stdin.readline

def dfs_recursive(graph, start, cnt = 0):
    visited[start]=cnt
    for node in graph[start]:
        if visited[node] == -1:
            dfs_recursive(graph, node, cnt+1)

if __name__=="__main__":
    
    N, M, R = map(int, input().split()) # 정점의 수 N, 간선의 수 M, 시작 정점 R
    
    graph = defaultdict(list) # value가 list인 딕셔너리 
    visited = [-1] * (N+1)   

    for _ in range(M):
        u, v = map(int, input().split()) #간선정보: 정점 u, 정점 v
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1,N+1):
        graph[i].sort(reverse = True)
        
    dfs_recursive(graph, R)
    
    for i in range(1, N+1):
        print(visited[i])

