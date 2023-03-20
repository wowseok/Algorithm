import sys

input =sys.stdin.readline

arr = []
for i in range(int(input())):
	x, y = map(int,input().split())
	arr.append((x,y))

arr.sort(key = lambda x : (x[1], x[0]))

for i in arr:
	print(i[0], i[1])