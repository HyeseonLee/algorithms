import sys

def solution(): # O(N^4)
    # dfs 함수
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    def dfs(x,y,count): # O(N^2)
        # 1. 체크인
        visited[x][y] = True
        count += 1 # dfs에 들어왔다는 것 자체가 집이 하나가 있다는 뜻이자나?

        # 2. 목적지인가?
        # 3. 인접한 것들 순회
        for i in range(4): # 위 아래 왼 오 돌면서 봅시다
            newX = x+dx[i]
            newY = y+dy[i]
            # 4. 방문할 수 있는가?
            if house[newX][newY]==1 and not visited[newX][newY]:
                # 5. 방문하기
                count = dfs(newX, newY,count)
                
        # 6. 체크아웃
        return count

    # 1. 입력값 받아서 house, visited 그래프 준비하기
    n = int(sys.stdin.readline().strip())
    MAX = n+5
    house = [[False]*(MAX) for _ in range(MAX)] # O(N^2)
    visited = [[False]*(MAX) for _ in range(MAX)] # O(N^2)

    # O(N^2)
    for i in range(n):
        line = sys.stdin.readline().strip()
        for j in range(n):
            house[i+1][j+1] = int(line[j])

    # line = ['0110100', '0110101', '1110101', '0000111', '0100000', '0111110', '0111000']
    # for idx, item in enumerate(line):
    #     print("item", item)
    #     for j in range(n):
    #         house[idx+1][j+1] = int(item[j])    


    
    # 2. 탐색 가보자고 ~
    danji = []
    danji_num = 0

    # O(N^4)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if house[i][j]==1 and not visited[i][j]:
                house_num = dfs(i,j,0) 
                danji.append(house_num)
                danji_num += 1

    print(danji_num) # 또는 len(danji)
    print(*sorted(danji), sep="\n") # nlog(n)
    
    

if __name__ == "__main__":
    solution()