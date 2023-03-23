import sys

input = sys.stdin.readline
from math import inf

N, M, B = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
INF = inf


min_value = min([min(i) for i in matrix]) # 각 행의 최소값을 리스트에 추가 후 min_value 후보들을 다시 min함수를 사용해 전체 matrix의 최소값 반환   
max_value = max([max(i) for i in matrix]) # 각 행의 최대값을 리스트에 추가 후 max_value 후보들을 다시 max함수를 사용해 전체 matrix의 최대값 반환



def check(matrix, current, inventory):
    number_one_task_time = 0
    number_two_task_time = 0
    for i in range(N): #세로 
        for j in range(M): #가로
            z = matrix[i][j] - current
            if z> 0:
                inventory += z #그 양만큼 인벤토리에 차게됨 -> 평탄화작업
                number_one_task_time  += 2*z #채우는 시간은 2배만큼 
            else: #0보다 작은 경우
                number_two_task_time += -z
    if inventory < number_two_task_time: #인벤토리 개수보다 c가 많으면 불가능
        return INF
    return number_one_task_time + number_two_task_time
    
    
max_second = INF
max_lv = 0 
for i in range(max_value, min_value-1, -1): # 같은 시간일 때,  가장 높은 기준높이를 사용하기위해서 max_value를 시작 인덱스로 한다.
    second = check(matrix, i, B)
    if max_second > second:
        max_second = second
        max_lv= i
print(max_second, max_lv)
