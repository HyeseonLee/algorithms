import sys
from collections import deque 

def solution():
    def bfs(n):
        # 0. 큐 만들고 체크인
        q = deque([n])
        visited[n] = True
        time[n] = 0

        while q:
            # 1. 큐에서 뽑기
            v = q.popleft()
            # print("방문 v", v)

            # 2. 목적지인가? : v(수빈이 위치)가 동생 위치와 같나?
            if v == k:
                return time[k]
            
            # 3. 인접하는 곳 순회
            dx = [+1, -1, +v]
            
            for i in range(3):
                newN = v+dx[i]
                # 4. 갈 수 있나?
                if newN >= 0 and newN <= 10**5 and not visited[newN]:
                    # 5. 체크인
                    visited[newN] = True
                    time[newN] = time[v]+1
                    # 6. 큐에 넣기
                    q.append(newN)
        return None

    n,k = map(int, sys.stdin.readline().strip().split())
    MAX = 10**5+1
    time = {i:0 for i in range(MAX)}
    visited = [False for _ in range(MAX)]

    result = bfs(n)

    return result

if __name__ == "__main__":
    print(solution())