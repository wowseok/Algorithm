import sys
import math

input = sys.stdin.readline
A, B, V = map(int, input().split())
day = (V-B) / (A-B)
print(math.ceil(day))