import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs_stack(graph, start):
    global cnt 
    from collections import deque
    
    visited = [0] * (N+1)     # 0번째 인덱스 사용 X
    need_visited = deque()
    
    need_visited.append(start)
    
    while need_visited:
        node = need_visited.pop()
    
        if visited[node] == 0:
            cnt += 1
            
            visited[node] = cnt
            need_visited.extend(graph[node])
    
    return visited[1:]
    
if __name__ == "__main__":
    
    N, M, R = map(int, input().split())
    graph = defaultdict(list)
    cnt = 0
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    
    for i in range(1, N+1):
        graph[i].sort()
    
    dfs_answer = dfs_stack(graph, R)
    
    for i in range(len(dfs_answer)):
        print(dfs_answer[i])

