import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    floor = int(input())    #층
    th = int(input())       #호
    arr = [j for j in range(1, th+1)]
    
    for k in range(1, floor+1): 
        for a in range(1, th):
            arr[a] += arr[a-1]
    print(arr[th-1])