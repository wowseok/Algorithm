def solution(k, m, score):
    answer = 0
    
    score.sort()
    
    r =len(score) % m
    
    
    for i in range(r): #남는 사과만큼 버리기
        score.pop(0)
    
    for i in range(0,len(score),m):
        answer = answer + score[i]*m
        

    return answer