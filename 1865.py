import sys

def bellman_ford(N, edges):
    # 무한대를 의미하는 큰 수
    INF = float('inf')
    # 초기 거리 설정 (모든 지점까지의 거리를 무한대로 설정)
    dist = [INF] * (N + 1)
    dist[1] = 0  # 시작 지점을 임의로 1로 설정
    
    # N-1번 반복하여 최단 거리 갱신
    for _ in range(N-1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # N번째 반복에서 갱신이 발생하면 음의 사이클 존재
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return True
    return False


tc = int(sys.stdin.readline().strip())
results = []

for _ in range(tc):
  n,m,w = map(int, sys.stdin.readline().strip().split())
  edges = [] 
  # 도로 정보 입력
  for _ in range(m):
      s,e,t = map(int, sys.stdin.readline().strip().split())
      edges.append((s, e, t))
      edges.append((e, s, t))
  
  # 웜홀 정보 입력
  for _ in range(w):
      s,e,t = map(int, sys.stdin.readline().strip().split())
      edges.append((s, e, -t))
  
  if bellman_ford(n, edges):
      results.append("YES")
  else:
      results.append("NO")

for result in results:
  print(result)

