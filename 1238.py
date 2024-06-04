import sys
import heapq

def solution():
    n,m,x = map(int, sys.stdin.readline().strip().split())
    graph = {}
    for _ in range(m):
        s,e,t = map(int, sys.stdin.readline().strip().split())
        if s in graph:
            graph[s].append((e,t))
        else:
            graph[s] = [(e,t)]
    

    def dij(start):
        dist = [int(1e9)] * (n+1)
        dist[start] = 0

        q = []
        heapq.heappush(q, (0,start)) # (가중치, node)

        while q:
            cur_dist, cur_node = heapq.heappop(q)

            # 무의미하면 continue
            if cur_dist > dist[cur_node]:
                continue

            # 순회하면서 업데이트
            if cur_node in graph:
                for next_node, next_dist in graph[cur_node]:
                    # 유의미한가?
                    cost = cur_dist + next_dist
                    if cost < dist[next_node]:
                        dist[next_node] = cost
                        heapq.heappush(q, (cost, next_node))
            
        return dist

    dist_back = dij(x)

    res = []
    for student in range(1,n+1): 
        dist_go = dij(student)
        heapq.heappush(res, -(dist_go[x] + dist_back[student]))
    
    print(-heapq.heappop(res))

if __name__ == "__main__":
    solution()