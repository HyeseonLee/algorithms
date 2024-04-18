# 1≤  입국 심사를 기다리는 사람 수 N ≤ 10^9
# 1 ≤ 각 심사관이 한 명을 심사하는데 걸리는 시간 M ≤ 10^9
# 1 ≤ 심사위원 수 L ≤ 10^5


def solution(n, times): # O(Llog)
    min_time = 0

    start, end = 1, n*max(times) # O(NL)

    while start<=end: # O(logNL)
        mid = (start+end)//2

        # 입국 심사 가능한 명수 계산
        people = 0
        for time in times: # O(L)
            people += mid//time
        
        # 심사 대기 인원의 모든 심사 종료
        if people >= n:
            min_time = mid
            end = mid-1
        else:
            start = mid+1

    return min_time


if __name__ == "__main__":
    print(solution(6, [7,10]))
