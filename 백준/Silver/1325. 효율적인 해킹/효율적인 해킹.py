import sys

from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())

def bfs(start):
	cnt = 1
	need_visited = deque([start])
	visit = [False for _ in range(N+1)]
	visit[start] = True

	while need_visited:
		node = need_visited.popleft()

		for i in graph[node]:
			if not visit[i]:
				visit[i] = True
				cnt += 1
				need_visited.append(i)

	return cnt

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split()) 
    graph[v].append(u)

max_cnt = 1
answer = []

for i in range(1,N+1):
	cnt = bfs(i)
	if cnt > max_cnt:
		max_cnt = cnt
		answer.clear()
		answer.append(i)
	elif cnt == max_cnt:
		answer.append(i)

print(*answer)