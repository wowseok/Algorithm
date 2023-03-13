import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs_recursive(graph,start, visited = []):
    visited.append(start)
    
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node)
    return visited
    
    
def bfs_stack(graph, start):
    from collections import deque
    
    visited = []
    need_visited = deque()
    
    need_visited.append(start)
    while need_visited:
        node = need_visited.popleft()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
        
        
    
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node)
    return visited

if __name__ == "__main__":
    N, M, V = map(int, input().split()) #정점의 개수 N, 간선의 개수 M, 시작노드 V
    
    graph = defaultdict(list)
    
    
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    for i in range(1, N+1): #정점의 개수만큼 정렬 
        graph[i].sort()
    
    
    dfs_answer = ' '.join(map(str, dfs_recursive(graph, V)))
    bfs_answer = ' '.join(map(str, bfs_stack(graph, V)))
    print(dfs_answer)
    print(bfs_answer)