import sys
from collections import defaultdict
from collections import deque 

input = sys.stdin.readline

def bfs(graph, start):
    cnt = 1
    visited = [0] * (N+1)
    need_visited = deque()
    need_visited.append(start)
    
    while need_visited:
        node = need_visited.popleft()
        if visited[node]  == 0:
            visited[node] = cnt
            need_visited.extend(graph[node])
            cnt+=1
    return visited
    

if __name__ == "__main__":
    N, M, R = map(int, input().split())
   
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    for i in range(1, N+1):
        graph[i].sort()

    answer = bfs(graph, R)
    for i in range(1, N+1):
        print(answer[i])