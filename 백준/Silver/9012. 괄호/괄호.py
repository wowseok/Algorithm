import sys

T = int(sys.stdin.readline())

for i in range(T):
    stack = []
    input_data = sys.stdin.readline().rstrip()
    for j in input_data:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack: # stack이 비어있지 않다면
                stack.pop()
            else: #스택이 비어있다면(여는 괄호가 없다면)
                print("NO")
                break
    else: #break문으로 끊기지 않았을 때 수행
        if not stack: #스택이 비어있다면
            print("YES")
        else: #스택이 남아있을떄
            print("NO")