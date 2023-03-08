import sys

N = int(sys.stdin.readline())

queue = list() # deque 사용가능
for i in range(N):
    cmd = sys.stdin.readline()
    
    if "push" in cmd:
        queue.append(int(cmd.split(' ')[1]))
    elif "front" in cmd:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif "back" in cmd:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif "size" in cmd:
        print(len(queue))
    elif "empty" in cmd:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif "pop" in cmd:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))