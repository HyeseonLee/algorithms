import sys

def solution():
    t = int(sys.stdin.readline().strip())
    answer_memo = []
    answer_tab = []

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        dp_m = [-1] * (n+1)
        # dp[0] = 1 # 이 문제에선 n이 양수이기에 이거 필요 없음

        def sol(n):
            if n<0:
                return 0
            if n==0:
                return 1
            
            if dp_m[n] != -1:
                return dp_m[n]
            
            dp_m[n] = sol(n-1)+sol(n-2)+sol(n-3)
            return dp_m[n]
        
        ans = sol(n)
        answer_memo.append(ans)

        ## 표 방식
        dp_t = [0]*(n+1)
        dp_t[0] = 1
        def tab(n):
            for i in range(1, n+1):
                if i>=1:
                    dp_t[i] += dp_t[i-1]
                if i>=2:
                    dp_t[i] += dp_t[i-2]
                if i>=3:
                    dp_t[i] += dp_t[i-3]
            return dp_t[n]

        ans2 = tab(n)
        answer_tab.append(ans2)
    

    # 결과 값 출력
    for item in answer_memo:
        print(item)

    for item in answer_tab:
        print(item)

    return None

if __name__ == "__main__":
    solution()