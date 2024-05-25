import sys

def solution():
    n = int(sys.stdin.readline().strip())
    couns = [0] #day1을 index1로 계산하려고
    for _ in range(n):
        item = list(map(int, sys.stdin.readline().strip().split()))
        couns.append(item)
    dp = [0] * (n+1+1)

    for d in range(n, 0, -1):
        if d + couns[d][0] > n+1:
            dp[d] = dp[d+1]
        else:
            dp[d] = max(couns[d][1]+dp[d+couns[d][0]], dp[d+1])
        
    return(max(dp))

if __name__ == "__main__":
    print(solution())