import sys
import heapq

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))
        graph[e].append((s, c))
    
    def dijkstra(start):
        dist = [int(1e9)] * (n + 1)
        dist[start] = 0
        
        q=[]
        heapq.heappush(q, (0,start))
        
        while q:
            cur_dist, cur_node = heapq.heappop(q)

            # 무의미하면 continue
            if cur_dist > dist[cur_node]:
                continue

            # 순회하면서 업데이트
            for next_node, next_dist in graph[cur_node]:
                # 유의미한가?
                cost = cur_dist + next_dist
                if cost < dist[next_node]:
                    dist[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
        
        return dist[n]
    
    result = dijkstra(1)
    print(result)
    
if __name__ == "__main__":
    solution()