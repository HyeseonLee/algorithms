import sys

def solution():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    dp = [1]*n

    for i in range(n-2, -1, -1):
        for k in range(i+1,n):
            if a[i]>a[k]:
               dp[i] = max(dp[i], dp[k]+1)
    
    return max(dp)


if __name__ == "__main__":
    print(solution())