import sys
from collections import deque
sys.setrecursionlimit(10**6) #python 내장 recursion 횟수가 적어서 이걸 꼭 해주자.

def dfs(graph, visited, v):
    # 1. 체크인
    visited[v] = True
    print(v, end=" ")

    # 2. 목적지인가 => 이 문제는 해당 안됨

    # 3. 연결된 곳 순회
    for i in range(1, len(graph[v])):
        # 4. 갈 수 있는가?
        if graph[v][i] and not visited[i]:
            # 5. 간다.
            dfs(graph, visited, i)

    # 6. 체크아웃 => 이 문제는 해당 안됨

def bfs(graph, visited, v):
    q = deque([v])
    visited[v] = True

    while q:
        # 1. 큐에서 꺼낸다.
        v = q.popleft()        
        print(v, end=" ")

        # 2. 목적지인가 => 이 문제는 해당 안됨
        
        # 3. 연결된 곳 순회
        for i in range(1, len(graph[v])):
            # 4. 갈 수 있는가
            if graph[v][i] and not visited[i]:
                # 5. 체크인
                visited[i] = True
                # 6. 큐에 넣는다.
                q.append(i)


def solution():
    n, m, v = map(int, sys.stdin.readline().strip().split())
    
    # 1. 그래프 초기화(인접행렬)
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    dfs_visited = [False] * (n + 1) 
    bfs_visited = [False] * (n + 1)
    # test = [[1,2],[1,3],[1,4],[2,4],[3,4]]
    # for item in test:
    #     a, b = item[0], item[1]
    #     graph[a][b] = graph[b][a] = True

    # 2. input 값을 토대로 그래프 그리기
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a][b] = graph[b][a] = True
        
    # 3. 레츠고
    dfs(graph, dfs_visited, v)
    print()
    bfs(graph, bfs_visited, v)


if __name__ == "__main__":
    solution()
