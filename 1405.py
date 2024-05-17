import sys

def solution():
    answer = []
    n_arr = list(map(int, sys.stdin.readline().strip().split()))
    n = n_arr[0]
    ALPHA = 5
    START = n//2
    dir_pro = list(map(lambda x: x/100 if x!= 0 else 0, n_arr[1:]))
    visited = [ [False]*(n*2+ALPHA) for _ in range(n*2+ALPHA)]


    def robot(x,y,pro,ans):
        #1. 체크인

        #2. 종료 조건
        if len(ans)==n: # N개의 경로를 다 방문하면, 확률을 결과에 더하기
            answer.append(pro)
            # print("ans", ans, "pro", pro, "answer", answer)
            return
        
        #3. 갈 수 있는 곳 순회
        dir = [[1,0], [-1,0], [0,1], [0,-1]] # E, W, S, N

        for d in range(4):
            # 동, 서, 남, 북 순서로 new_x, new_y 만들기
            new_x = x+dir[d][0]
            new_y = y+dir[d][1]
            #4. 갈 수 있나?

            if not visited[new_x][new_y] and dir_pro[d]!=0:
                #5. 가자
                visited[x][y] = True
                # 단순한 경로가 나올 확률 계산하기
                pro = pro*dir_pro[d] 
                # 경로 추가하기
                ans.append(d)
                robot(new_x, new_y, pro, ans)
                ans.pop()
                visited[new_x][new_y] = False
                pro = pro/dir_pro[d] 
            else: 
                pass
        #6. 체크아웃

    robot(START, START,1,[])

    return sum(answer)

if __name__ == "__main__":
    print(solution())