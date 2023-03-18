import sys
from collections import defaultdict
from collections import deque 

input = sys.stdin.readline

def bfs(graph, start):
    depth = 0
    depth_list = [-1] * (N+1)
    visited = [0] * (N+1)
    
    visited[start] = True
    need_visited = deque([(start, depth)])
    
    while need_visited:
        start, depth = need_visited.popleft()
        depth_list[start] = depth
        for node in graph[start]:
            if visited[node]  == 0:
                visited[node] = True
                need_visited.append((node, depth+1))
            
    return depth_list
    

if __name__ == "__main__":
    N, M, R = map(int, input().split())
   
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    for i in range(1, N+1):
        graph[i].sort(reverse = True)

    answer = bfs(graph, R)
    for i in range(1, N+1):
        print(answer[i])