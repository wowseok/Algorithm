import sys
n, m = map(int, sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
B = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]


for i in range(n):
    for j in range(m):
        A[i][j] += B[i][j]

for i in A:
    print(*i)