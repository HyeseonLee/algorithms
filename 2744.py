import sys
import heapq
def solution():
    n = int(sys.stdin.readline().strip())
    a, b = map(int, sys.stdin.readline().split())
    v = int(sys.stdin.readline().strip())

    # 1. 그래프 만들기
    graph = {i : [] for i in range(1,n+1)}
    
    for _ in range(v):
        x,y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    
    # 2. 다익스트라 최단거리 테이블 초기화

    dist = [int(1e9) for _ in range(n+1)]
    dist[a] = 0

    # 3. 최단거리 구하기 
        # a에서 b까지 가는 최단 거리를 구해야해. 
        # 만약 그것이 int(1e9)이 아니라면 최단거리가 있다는 것이니까 그걸 출력, 
        # 맞다면 최단거리가 없다는 것이니까 -1 출력
    
    # 3-1. 큐 만들기, heapq에 시작 지점 정보 넣기
    q = []
    heapq.heappush(q, (0,a)) # (거리, 노드)

    # 3-2. q를 돌면서 그래프 정보를 가지고 최단거리테이블 갱신
    while q:
        # 1. 큐에서 노드를 꺼내서
        cur_dist, node = heapq.heappop(q)
        # 2. 지금 dist가 무의미한지 판단 : node까지 가는데 필요한 가중치 값이 최단거리테이블의 값보다 크다면 거기를 들릴 필요가 없음
        if cur_dist > dist[node]:
            continue
        # 3. 그 노드에서 갈 수 있는 노드들 순회
        for next_node in graph[node]:
            # 4. 최단거리 테이블 갱신
            cost = cur_dist + 1
            if cost < dist[next_node]:
                dist[next_node] = cost
                # 5. 큐에 넣기
                heapq.heappush(q, (cost, next_node))
    
    # b까지 가는 최단 거리가
    if dist[b] != int(1e9):
        return dist[b]
    else:
        return -1

if __name__ == "__main__":
    print(solution())
