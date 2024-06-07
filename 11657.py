import sys
from collections import deque
def solution():
    n,m = map(int, sys.stdin.readline().strip().split())
    graph = {i:[] for i in range(1,n+1)}
    for _ in range(m):
        a,b,c = map(int, sys.stdin.readline().strip().split())
        graph[a].append((b,c))
    
    # print(graph)

    def dij(start):
        dist = [int(1e9)]*(n+1)
        dist[start] = 0

        count = [0]*(n+1)

        q = deque([start])
        in_queue = [False]*(n+1)
        in_queue[start] = True

        while q:
            node = q.popleft()
            in_queue[node] = False

            # node에서 연결된 곳 돌면서 최단거리 업데이트
            for next_node, next_dist in graph[node]:
                cost = dist[node] + next_dist
                if cost<dist[next_node]:
                    dist[next_node] = cost
                    if not in_queue[next_node]: # next_node가 큐에 없으면
                        q.append(next_node)
                        in_queue[next_node] = True

                        # 음의 사이클 감지
                        count[next_node] += 1 # queue에 넣을 대 마다 count 더하기
                        if count[next_node]>n-1:
                            print("-1")  # 음의 사이클 존재
                            return
        # 모든 최단거리가 업데이트 되었다.
        for i in range(2,n+1):
            if dist[i] != int(1e9):
                print(dist[i])
            else:
                print("-1")
        return
    # 1번 도시에서 출발해서 나머지 도시로 가는 정보 출력
    dij(1)
    return None

if __name__=="__main__":
    solution()