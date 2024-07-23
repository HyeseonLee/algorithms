import sys
from collections import deque

def bfs(n,m,graph):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    
    queue = deque([(0, 0, 0)]) 
    visited[0][0][0] = 1  
    
    while queue:
        x, y, broken = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[x][y][broken]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][broken] == 0: # 갈 수 있는 곳인 0인 경우
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))
                elif graph[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0: # 벽인 곳인 1인 경우에, broken 횟수가 1이고, 방문 가능할 경우
                    visited[nx][ny][1] = visited[x][y][broken] + 1
                    queue.append((nx, ny, 1))
    
    return -1


n,m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

result = bfs(n,m,graph)
print(result)
