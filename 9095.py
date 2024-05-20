import sys

def solution():
    t = int(sys.stdin.readline().strip())
    answer = []

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        dp = [-1] * (n+1)
        dp[0] = 1

        def sol(i):
            if i<0:
                return 0
            if i==0:
                return 1
            
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = sol(i-1)+sol(i-2)+sol(i-3)
            return dp[i]
        
        ans = sol(n)
        answer.append(ans)

    return print(**answer)

if __name__ == "__main__":
    solution()