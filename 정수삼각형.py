def solution(triangle):
    answer = 0
    arr_len = len(triangle[-1])
    
    # 연산 편의성 위해 triangle에 0 채우기 => 불필요 !!
    # for i in range(arr_len):
    #     for _ in range(arr_len-1-i):
    #         triangle[i].append(0)

    # 반복 연산을 피하기 위해 dp 만들기
    dp = [[0]*(arr_len) for _ in range(arr_len)]
    dp[0][0] = triangle[0][0]

    # 누적 합 구하기
    for i in range(1,arr_len):
        for j in range(i+1):
            if j<1:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif i==j:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else: 
                dp[i][j] = max(triangle[i][j] + dp[i-1][j-1], triangle[i][j]+dp[i-1][j])

    # 정답은 ~ 
    answer = max(dp[-1])
          
    return answer

if __name__ == "__main__":
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))