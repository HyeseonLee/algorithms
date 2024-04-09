import sys

N, K = map(int, sys.stdin.readline().split())

queue = [str(i) for i in range(1,N+1)] # O(N)

print('<', end="")
while len(queue)>1: 
    for _ in range(K-1): # O(NK) # K번째가 맨 앞에 오게 만들기
        queue.append(queue[0])
        if not queue:
            print("queue is empty")
        else:
            queue.pop(0) # O(N)
    print(queue[0], end=", ")
    if not queue:
            print("queue is empty")
    else:
        queue.pop(0) # O(N)
print(queue[0], end="")
print(">", end="")
