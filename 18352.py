import sys
from collections import deque

def solution():
    n,m,k,x = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(n+1)] # 어떤 노드가 어떤 노드랑 연결 되어 있는지 저장하는 graph 
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b) # 단방향 그래프 (a->b)
    
    res = []

    # x부터 시작해서 도달할 수 있는 도시까지 가기
    visited = [False] * (n+1)
    visited[x] = True

    q = deque([(x,0)]) # (노드, 거리)

    while q:
        #1. 큐에서 꺼낸다.
        node, dist = q.popleft()

        #2. 목적지인가?
        if dist == k:
            res.append(node)
        
        #3. 순회할 수 있는 곳 돌기
        for next_node in graph[node]: # graph[node]에는 node에서 갈 수 있는 노드가 저장되어 있음
            #4. 갈 수 있나?
            if not visited[next_node]:
                #5. 체크인
                visited[next_node] = True
                #6. 큐에 넣기
                q.append((next_node, dist+1))
    
    if res:
        res.sort()
        for r in res:
            print(r)
    else:   
        print(-1)


if __name__ == "__main__":
    solution()