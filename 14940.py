import sys
from collections import deque

def solution():
    def bfs(start_y, start_x):
        q = deque([(start_y, start_x)])
        res[start_y][start_x] = 0
        
        dy = [0, 0, 1, -1]
        dx = [1, -1, 0, 0]

        while q:
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and res[ny][nx] == -1:
                    if graph[ny][nx] == 1:
                        res[ny][nx] = res[y][x] + 1
                        q.append((ny, nx))
                    elif graph[ny][nx] == 0:
                        res[ny][nx] = 0

    n, m = map(int, sys.stdin.readline().strip().split())
    graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    res = [[-1] * m for _ in range(n)]

    start_y, start_x = None, None
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 2:
                start_y, start_x = y, x
                break
        if start_y is not None:
            break

    bfs(start_y, start_x)

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 0:
                res[y][x] = 0

    for item in res:
        print(' '.join(map(str, item)))

if __name__ == "__main__":
    solution()
