n = int(input())
answer = 0
for i in range(n):
    a=input()
    if list(a) == sorted(a, key=a.find):
        answer+=1
print(answer)        
        