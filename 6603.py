import sys
sys.setrecursionlimit(10**6)

# dfs - backtraking 방법
def dfs_backtracking(s, idx, ans):
    # 2. 목적지인가? 6개 로또 번호를 탐색함
    if len(ans)==6:
        print(*ans)
        return 
    
    # 3. 인접한 곳 돌기
    for i in range(idx+1, len(s)):
        # 4. 갈 수 있나?
        if s[i] not in ans:
            # 1. 체크인
            ans.append(s[i])
            # 5. 가자.
            dfs_backtracking(s,i,ans)
            ans.pop()

# dfs - 새로운 리스트 만드는 방법
def dfs_new_list(s,idx,ans):
    global result
    # 1. 체크인
    ans = ans+[s[idx]]

    # 2. 목적지인가?
    if len(ans)==6:
        form = ' '.join(map(str, ans))
        result.append(form)
        # print(*ans)
        return
    
    # 3. 인접한 곳 돌기
    for i in range(idx+1, len(s)):
        # 4. 갈 수 있나?
        if s[i] not in ans:
            # 5. 가자.
            dfs_new_list(s,i,ans)


# 숫자 조합을 만들어야 함 = 파고 드는 경로가 중요함 (dfs)
def solution():
    # 1. 입력 값 받기
    tc = []
    while True:
        line = sys.stdin.readline().strip()
        if line[0] == '0':
            break
        
        # 이걸 어떻게 저장하지?
            # line[0] : k개의 수
            # line[1:] : 집합 S

        # k = int(line[0])
        # s = list(map(int, line[1:].split()))

        parts = list(map(int, line.split()))
        k = parts[0]
        s = parts[1:]
        tc.append({'k':k, 's':s})
    
    # 2. 세팅
    result = []

    for i in range(len(tc)):
        k = tc[i]['k']
        s = tc[i]['s']
        
        # 새로운 리스트 방식
        for idx, num in enumerate(s):
            dfs_new_list(s,idx,[])
        
        # 백트래킹 방식
        # for idx_ in range(len(s)):
        #     dfs_backtracking(s,idx_,[s[idx_]])

        result.append("") # 빈줄 추가

    result.pop() # 빈줄 제거 

    print('\n'.join(result))




if __name__ == "__main__":
    solution()