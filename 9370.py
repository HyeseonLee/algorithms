import sys
import heapq

def solution():
    def dij(start):
        # 최단거리 테이블 초기화
        dist = [int(1e9) for _ in range(n+1)]
        dist[start] = 0
        q = []
        heapq.heappush(q,(0, start)) # (거리, start)

        while q:
            cur_dist, cur_node = heapq.heappop(q)

            if cur_dist > dist[cur_node]:
                continue
            
            # 갈 수 있는 곳 순회
            for next_node, next_dist in graph[cur_node]:
                cost = cur_dist + next_dist
                if cost<dist[next_node]:
                    dist[next_node] = cost
                    heapq.heappush(q,(cost, next_node))
        return dist
    
    T = int(sys.stdin.readline().strip())
    results = []

    for _ in range(T):
        n,m,t = map(int, sys.stdin.readline().split())
        s,g,h = map(int, sys.stdin.readline().split())
        graph = {i : [] for i in range(1,n+1)}
        tc_ans = []
        
        g_h_dist = None
        for _ in range(m):
            a,b,d = map(int, sys.stdin.readline().split())
            graph[a].append((b,d)) # b 까지 가는데 가중치 d
            graph[b].append((a,d)) # a 까지 가는데 가중치 d # 양방향 그래프
            # g to h dist
            if (a == g and b == h) or (a == h and b == g):
                g_h_dist = d

        candidates = []
        for _ in range(t):
            c = int(sys.stdin.readline().strip())
            candidates.append(c)

        fromS_dist = dij(s)
        fromG_dist = dij(g)
        fromH_dist = dij(h)
        
        for c in candidates:
            # 목적지까지 가는데 g-h, h-g를 방문하는 2가지 케이스 가능
            # fromGToH_dist = fromS_dist[g]+g_h_dist+fromH_dist[c]
            # fromHToG_dist = fromS_dist[h]+g_h_dist+fromG_dist[c]
            
            # s부터 시작해서 구한 c의 최단 거리가 g-h를 거친 최단 거리 or h-g를 거친 최단 거리와 동일하다면 유효한 목적지 ! 
            if (fromS_dist[c] == fromS_dist[g]+g_h_dist+fromH_dist[c]) or (fromS_dist[c] == fromS_dist[h]+g_h_dist+fromG_dist[c]):
                tc_ans.append(c)

        tc_ans.sort()
        results.append(tc_ans)
    
    for res in results:
        print(" ".join(map(str, res)))

if __name__ == "__main__":
    solution()
