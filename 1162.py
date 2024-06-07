import sys 
import heapq # 다익스트라는 힙큐

def solution():
    n,m,k = map(int, sys.stdin.readline().strip().split())
    graph = {i:[] for i in range(1,n+1)}
    for _ in range(m):
        s,e,c = map(int, sys.stdin.readline().strip().split())
        graph[s].append((e,c))
        graph[e].append((s,c))
    
    def dij(start):
        dist = [[float("inf")]*(k+1) for _ in range(n+1)]
        for i in range(k+1):
            dist[start][i] = 0

        q = []
        heapq.heappush(q, (0,start,0)) # (가중치, 노드, 포장횟수)

        while q:
            cur_dist, cur_node, cur_paved = heapq.heappop(q)

            if cur_dist>dist[cur_node][cur_paved]:
                continue

            for next_node, next_dist in graph[cur_node]:
                # 포장 하는 경우
                if cur_paved<k:
                    cost = 0 + cur_dist
                    if cost<dist[next_node][cur_paved+1]:
                        dist[next_node][cur_paved+1] = cost
                        heapq.heappush(q, (cost, next_node, cur_paved+1))

                # 포장 안하는 경우
                cost = next_dist + cur_dist
                if cost < dist[next_node][cur_paved]:
                    dist[next_node][cur_paved] = cost
                    heapq.heappush(q, (cost, next_node, cur_paved))

        return min(dist[n]) # k이하의 상황들 중 가장 최단거리가 정답
    
    res = dij(1)
    print(res)

if __name__ == "__main__":
    solution()