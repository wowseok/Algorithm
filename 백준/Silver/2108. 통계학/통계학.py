import sys
from collections import defaultdict 
input=sys.stdin.readline

n=int(input())
arr=[]


for i in range(n):
    arr.append(int(input()))
    
print(round(sum(arr)/len(arr))) #산술평균 round를 써서  소수점 이하 첫째 짜리에서 반올림한다.

arr.sort()
print(arr[len(arr)//2])# 중앙값


dic=defaultdict(int)    #최빈값
result = []
for i in arr:       
    dic[i]+=1

target = max(dic.values())

for key, value in dic.items():
    if value == target:
            result.append(key)
if len(result) == 1:
    print(result[0])

else:
    result.sort()
    print(result[1])
    
print(max(arr)-min(arr))