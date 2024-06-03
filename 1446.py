import sys
import heapq

def solution():
    n,d = map(int, sys.stdin.readline().strip().split())
    graph = {}
    for _ in range(n):
        s,e,cost = map(int, sys.stdin.readline().strip().split())
        if s in graph:
            graph[s].append((e,cost))        
        else:
            graph[s] = [(e,cost)]
    
    def dij(start):
        dist = [int(1e9)]*(d+1)
        dist[start] = 0

        q = []
        heapq.heappush(q, (0,0)) # dist, node

        while q:
            cur_dist, cur_node = heapq.heappop(q)

            if cur_dist>dist[cur_node]:
                continue
            
            # 다음 노드로 이동 (근데 d까지)
            next_node = cur_node+1
            next_dist = cur_dist+1
            if next_node<=d and next_dist<dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(q, (next_dist, next_node))
            
            if cur_node in graph:
                for n_node, n_dist in graph[cur_node]:
                    if n_node <= d:
                        cost = cur_dist + n_dist
                        if cost<dist[n_node]:
                            dist[n_node] = cost
                            heapq.heappush(q, (cost, n_node))
        return dist[d]
    
    ans = dij(0)
    print(ans)

if __name__ == "__main__":
    solution()