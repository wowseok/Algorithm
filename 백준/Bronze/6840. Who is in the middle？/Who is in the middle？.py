import sys

arr = []
for _ in range(3):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
print(arr[1])