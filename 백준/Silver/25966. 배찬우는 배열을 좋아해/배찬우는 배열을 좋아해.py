import sys

input = sys.stdin.readline

N, M, q = map(int, input().split()) #행의 개수, 열의 개수, 쿼리의 개수

arr = [list(map(int, input().split())) for _ in range(N)]

input_data = [list(map(int, input().split())) for i in range(q)]

for i in range(q):
    
    if len(input_data[i]) == 3:
        arr[input_data[i][1]], arr[input_data[i][2]] = arr[input_data[i][2]], arr[input_data[i][1]] # i j : i번 행과  j번 행을 swap한다.
    elif len(input_data[i]) == 4:
        arr[input_data[i][1]][input_data[i][2]] = input_data[i][3] #i번 행의 j번 열의 값을 k로 변경

for i in range(N):
    print(" ".join(map(str, arr[i])))
        
        