from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

queue = deque(range(1, N+1)) #O(N)
result = []

while queue: # O(N)
    for _ in range(K-1): # O(K)
        queue.append(queue.popleft())  # O(1)
    result.append(queue.popleft())  # O(1) K번째 숫자를 결과 리스트에 추가

print("<", end="")
print(*result, sep=", ", end="")
print(">")
