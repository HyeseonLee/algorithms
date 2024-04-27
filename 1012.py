import sys
from collections import deque

def bfs(y,x, graph, visited):
    #0. 큐 만들고 첫번째 값 체크인
    q = deque([(y,x)])
    visited[y][x] = True

    while q:
        #1. 큐에서 하나 뽑기
        v_y, v_x = q.popleft()

        #3. 4방향으로 갈 수 있는 곳 순회
        dy = [1,-1,0,0]
        dx = [0,0,1,-1]

        for i in range(4):
            newY = v_y + dy[i]
            newX = v_x + dx[i]

            #4. 갈 수 있나?
            if graph[newY][newX] == 1 and not visited[newY][newX]:
                #5. 체크인
                visited[newY][newX] = True    
                #6. 큐에 넣기
                q.append((newY,newX))


def solution():
    t = int(sys.stdin.readline().strip())
    ans = []
    for _ in range(t):
        m,n,k = map(int, sys.stdin.readline().strip().split())
        graph = [[0]*(m+5) for _ in range(n+5)]
        visited = [[False]*(m+5) for _ in range(n+5)]
        count = 0

        for _ in range(k): #O(k)
            x,y = map(int,sys.stdin.readline().strip().split())
            graph[y+1][x+1] = 1
        
        # 2. 배추 밭을 돌아봅시다.
        for i in range(1,n+1):
            for j in range(1,m+1):
                if graph[i][j]==1 and not visited[i][j]:
                    count += 1
                    bfs(i,j,graph,visited) #O((NM)^2)
        ans.append(count)
    print(*ans, sep="\n")
        
if __name__ == "__main__":
    solution()
