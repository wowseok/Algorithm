import sys

mn, mx = map(int,sys.stdin.readline().split())
check = [False] * (mx-mn+1)
answer = 0

i = 2
while (i**2 <= mx+1):
    mok = mn // (i ** 2) # min값을 i * i로 나눈 몫을 구한다.
    
    if (mn % (i ** 2)) != 0:
        mok += 1
    
    while(mok * (i ** 2) <= mx):
        
        check[mok * (i ** 2) - mn] = True; #True이면 제곱 ㅇㅇ수
        mok += 1 
    
    i+=1   

for i in range(mx-mn+1):
    if check[i] == False:
        answer+=1

print(answer)