import sys
from collections import deque
# visited가 필요 없다. 왜냐하면, 기존 토마토 이차원 배열을 바로 0->1로 변경해줄 것이기 때문!!
def bfs(ik,day,graph):
    # 익어있는 토마토들을 기준으로 bfs를 동시에 돌기 시작한다.
    # q = [(익어있는 곳 위치1,날짜), (익어있는 곳 위치2,날짜), (익어있는 곳 위치3,날짜)]
    # 이렇게 되어있는 상태인데, 그렇다면 익1의 근처 토마토 탐색 후 큐에 넣기 -> 익2의 근처 토마토 탐색 후 큐에 넣기 -> 익3의 근처 토마토 탐색 후 큐에 넣기 
    # 이런꼴로 돌아가기 때문에, 차례차례 돌아가면서 방문을 하게 되는 것이고 ! 중간에 만나는 경우도 대처 가능 !
    q = deque(ik)
    days = 0

    while q:
        #1. 큐에서 하나 뽑기
        v_y, v_x, day = q.popleft()
        days = day # 큐에서 마지막으로 뽑는 값의 day가 가지고 있는 것은 : 익히는데 걸린 날짜 수. 이렇게 days=day로 받지 않으면, while q: 이게 종료 되었을 때, 가장 마지막 day가 몇일이었는지 알 수가 없다. 그래서 이게 필요한거임
        
        #3. 근처 순회
        dy = [1,-1,0,0]
        dx = [0,0,1,-1]

        for i in range(4):
            newY = v_y + dy[i]
            newX = v_x + dx[i]
            #4. 갈 수 있나?
            if graph[newY][newX] == 0:
                #5. 체크인
                graph[newY][newX] = 1 # 토마토 익히기
                #6. 큐에 넣기
                q.append((newY, newX, day+1)) # 지금 방문한 토마토까지 오는 날짜는 4방향탐색의 중심 노드까지 오는 날짜+1이지요 ~ "A까지 오는 거리"="A 전에 까지 오는 거리 + 1"
    
    # 탐색 다 끝났는데 아직도 0인 곳이 있으면 -1 출력
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                return -1
            
    return days

def solution():
    m,n = map(int, sys.stdin.readline().strip().split())
    graph = [[-1]*(m+2)]
    visited = [[False]*(m+2) for _ in range(n+2)]
    day = []

    for _ in range(n):
        line = list(map(int,sys.stdin.readline().strip().split()))
        graph.append([-1] + line + [-1])
    graph.append([-1]*(m+2))

    ik = []
    num_0 = 0
    for y in range(1,n+1):
        for x in range(1,m+1):
            if graph[y][x] == 1:
                ik.append((y,x,0))
            elif graph[y][x] == 0:
                num_0 += 1
    

    # 이미 모든 토마토가 익어있음. 상황 종료. 
    if num_0 == 0:
        return(0)

    # 익어야 할 토마토가 있습니다 ! 탐색 시작하시죠 !
    # res = {i:deque([(ik[i][0], ik[i][1])]) for i in range(len(ik))}
    day = bfs(ik, day, graph)

    # 며칠이 걸리나요?
    return day
    
if __name__ == "__main__":
    print(solution())