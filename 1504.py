import sys
import heapq

def solution():
    res = -1

    n,e = map(int, sys.stdin.readline().strip().split())
    graph = {i:[] for i in range(1,n+1)}

    for _ in range(e):
        a,b,c = map(int, sys.stdin.readline().strip().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    v1,v2 = map(int, sys.stdin.readline().strip().split())

    # # 올바른 v1, v2인지 확인 => 보통 문제에서는 범위에 어긋난 입력값을 주지는 않기 때문에 이것까지 예외처리 할 필요는 없다.
    # if v1 == n or v2 == 1:
    #     return -1
    
    def dij(start):
        dist = [int(1e9) for _ in range(n+1)]
        dist[start] = 0
        q = [] 
        heapq.heappush(q,(0,start)) # (거리, 노드)
        while q:
            cur_dist, cur_node = heapq.heappop(q)

            if cur_dist>dist[cur_node]:
                continue
                
            for next_node, next_dist in graph[cur_node]:
                cost = cur_dist + next_dist
                if cost < dist[next_node]:
                    dist[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
        return dist
    
    from1_dist = dij(1)
    fromV1_dist = dij(v1)
    fromV2_dist = dij(v2)

    cand1 = from1_dist[v1] + fromV1_dist[v2] + fromV2_dist[n]
    cand2 = from1_dist[v2] + fromV2_dist[v1] + fromV1_dist[n]
    
    res = min(cand1,cand2)

    # 존재하지 않는 최단 거리는 int(1e9)로 초기화 되어 있다는 것을 까먹지말아요
    # 갈 수 있는 경로가 없음을 어떻게 판단하지 ? => res가 int(1e9)보다 같거나 클 때?
    if res<int(1e9):
        return res
    else:
        return -1

if __name__=="__main__":
    print(solution())