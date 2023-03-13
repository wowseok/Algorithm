import sys
from collections import defaultdict

def dfs_recursive(graph, start, visited = []):
    visited.append(start)
    
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node)
    return len(visited[1:])
    
    
if __name__ == "__main__":
    
    input = sys.stdin.readline
    com_number = int(input())
    edge = int(input())
    
    graph = defaultdict(list)
    for _ in range(edge):
        u, v= map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    dfs_answer = dfs_recursive(graph, 1)
    print(dfs_answer)
