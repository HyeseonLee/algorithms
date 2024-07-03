import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

m = len(s1)
n = len(s2)
# 1. dp 초기화, dp[i][j]는 s1의 i번쨰까지 오면서의 LCS 길이, s2의 j번쨰까지 오면서의 LCS 길이
dp = [[0]*(n+1) for _ in range(m+1)]

# 2. dp 점화식
for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[m][n]) # s1의 제일 마지막 글자까지 보고, s2의 제일 마지막 글자까지 저장 된 dp값이 두 문자열에 대한 LCS 길이다.
