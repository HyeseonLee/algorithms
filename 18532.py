import sys
from collections import deque

def solution():
    n,m,k,x = map(int, sys.stdin.readline().strip().split())
    
    road = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().strip().split())
        road[a].append(b)
    
    visited = [False] * (n+1)
    visited[x] = True
    q = deque()
    q.append((x,0))
    while q:
        node, dist = q.popleft()
        if dist == k:
            print(node)
            return
        for next_node in road[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, dist+1))
    print(-1)

    return None

if __name__ == "__main__":
    print(solution())