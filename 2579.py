import sys
import heapq
def solution():
    n = int(sys.stdin.readline().strip())
    s = [0]
    dp=[0]*(n+1)

    for _ in range(n):
        s.append(int(sys.stdin.readline().strip()))
    
    if n==1:
        print(s[1])
        return None
    elif n==2:
        print(s[1]+s[2])
        return None
    
    dp[0] = 0
    dp[1] = s[1]
    dp[2] = s[1]+s[2]
    
    for i in range(3,n+1):
        dp[i] = max(s[i]+s[i-1]+dp[i-3], s[i]+dp[i-2])
    
    print(dp[-1])
    
    
    return None

if __name__ == "__main__":
    solution()