import sys

input = sys.stdin.readline

N = int(input())

input_data = []
for i in range(N):
    input_data.append(input().split())


for j in range(len(input_data)):
    input_data[j] = input_data[j][::-1]
    print('Case #%d: %s' %(j+1, " ".join(input_data[j])))
