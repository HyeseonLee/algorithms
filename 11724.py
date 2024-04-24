import sys
from collections import deque
sys.setrecursionlimit(10**6)

# O(m+n)
def solution():
    def dfs(i): # O(m+n)
        # 1. 체크인
        visited[i] = True

        # 2. 목적지인가?
        # 3. 인접한 곳 순회
        for k in l[i]:
            # 4. 갈 수 있나?
            if not visited[k]:
                # 5. 방문하기
                dfs(k)

        # 6. 체크아웃
        return None
    
    def bfs(i):
        # 0. 큐 만들기
        q = deque([i])
        
        while q:
            # 1. 큐에서 뽑기
            v = q.popleft()
            # 2. 목적지 인가?
            # 3. 인접한 곳 순회
            for k in l[v]:
                # 4. 갈 수 있나?
                if not visited[k]:
                    # 5. 체크인
                    visited[k] = True
                    # 6. 큐에 넣기
                    q.append(k)

    # 1. 입력값 받기
    n,m = map(int, sys.stdin.readline().strip().split())

    # 2. 그래프 만들기 : 인접 리스트로 해볼까봐요 ~
    # 1<=u,v<=n 이라고 했으니까, u,v는 무조건 n보다 같거나 작은 수 -> 그래서 (n+1) 해줘야한다.
    l = {i:[] for i in range(n+1)}
    visited = [False]*(n+1)

    # for _ in range(m):
    #     u,v = map(int, sys.stdin.readline().strip().split())
    #     l[u].append(v)
    #     l[v].append(u)

    li = [[1,2], [2,5],[5,1],[3,4],[4,6]]
    for item in li:
        u,v = item[0], item[1]
        l[u].append(v)
        l[v].append(u)

    # 3. 탐색하면서 연결요소 개수를 세보자구요 ~
    count = 0
    for i in range(1,n+1):
        # 방문한 적 없는 정점 다 돌면서
        if not visited[i]:
            # dfs(i)
            bfs(i)
            count += 1 
            
    print(count)
    return None

if __name__ == "__main__":
    solution()