import sys

input = sys.stdin.readline
N = int(input())

if N == 0 :
    print(1)
else :
    result = 1
    for i in range(1, N+1) :
        result *= i
    print(result)