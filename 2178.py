import sys
from collections import deque

def bfs(y,x, graph, visited, count, n, m): # O((NM)^2)
        #0. 큐 만들고 첫번째 체크인
        q = deque([(y,x)])
        visited[y][x] = True
        count[y][x] += 1

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        while q:
            #1. 큐에서 꺼낸다.
            v_y, v_x = q.popleft()

            #2. 목적지인가?
            if v_y == n+1 and v_x == m+1:
                return
            
            #3. 순회할 수 있는 곳 돌기
            for i in range(4):
                newY = v_y + dy[i]
                newX = v_x + dx[i]
                #4. 갈 수 있나?
                if graph[newY][newX]==1 and not visited[newY][newX]:
                    #5. 체크인
                    visited[newY][newX] = True
                    count[newY][newX] = count[v_y][v_x] + 1
                    #6. 큐에 넣기
                    q.append((newY, newX))

def solution():
    # 1. 입력값 받고 세팅
    n,m = map(int, sys.stdin.readline().strip().split())
    graph = [[0]*(m+5) for _ in range(n+5)]
    visited = [[False]*(m+5) for _ in range(n+5)]
    count = [[0]*(m+5) for _ in range(n+5)]

    # O(NM)
    for i in range(n):
        line = list(map(int, sys.stdin.readline().strip()))
        for k in range(m):
            graph[i+1][k+1] = line[k]
    
    # 2. 미로 찾기 시작
    bfs(1,1, graph, visited, count, n, m)
    return count[n][m]

if __name__ == "__main__":
    print(solution())