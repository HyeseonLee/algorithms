import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

m = len(s1)
n = len(s2)

dp = [[0]*(n+1) for _ in range(m+1)]
lcs = []
for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i-1] == s2[j-1]: # 같다 # LCS에 추가
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i,j=m,n
while i>0 and j>0:
    if s1[i-1] == s2[j-1]:
        lcs.append(s1[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print(dp[m][n])
if len(lcs)!=0:
    print(''.join(lcs[::-1]))
