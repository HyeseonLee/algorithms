import sys

def solution():

    n = int(sys.stdin.readline().strip())
    ### 이 방법은 시간 복잡도가 쓰레기라 버리기 !
    # 나쁜 수열에 들어가있는 요소들 만들기, O(3^40)
    # n개 길이의 가능한 모든 수열 만들기 = 3^n , O(3^80) => 오 이거 최악인디???
    # 가능한 모든 수열에서 나쁜 수열인 것 제거하기
    # 남은 것 중에서 최소 값을 결과 값으로 출력하기
    

    ### New Solution
    # dfs로 돌면서 N자리 다 되었을 때 최종으로 확인해서 정답으로 만들거구요
    # 1부터 시작하면 -> (1)제외 2,3 방문 -> 2 방문시 (2)제외 1,3 방문 => 즉, 재귀 보낼 때 마다 visited를 초기화 해서 보내고, 체크인시 방문 시키는 것 !
    # 현재 ans에 저장된 길이 leng 기준으로, stand = leng//2, 2<= ? <= stand 범위에 있는 ? 길이가 두번 반복 되는지 확인. e.g., num[l+1-3:l+1] == l+1-3*2:l+1-3
    
    def is_bad(seq):
        leng = len(seq)
        for s in range(1,leng//2+1):
            if seq[leng-s*2:leng-s] == seq[leng-s:leng]:
                return True
        return False

    def dfs(ans): 
        if len(ans)==n:
            print(''.join(map(str, ans)))
            sys.exit(0)
        

        #3. 갈 수 있는 모든 곳 순회
        for i in "123":
            if not is_bad(ans+i):
                dfs(ans+i)

    dfs("")        
    
    return None

if __name__ == "__main__":
    print(solution())