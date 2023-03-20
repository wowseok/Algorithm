import sys

input = sys.stdin.readline
N = int(input())
arr = []

for i in range(N):
    w, h = map(int, input().split())
    arr.append([w, h])

for i in range(N):
    rank = 1
    for j in range(N):
        if (arr[i][0] < arr[j][0]) and (arr[i][1] <  arr[j][1]):
            rank += 1 
    print(rank, end = ' ')