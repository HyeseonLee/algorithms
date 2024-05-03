import sys

def solution():
    team = 0
    n,m,k = map(int, sys.stdin.readline().strip().split())
    collect_k = 0

    # 한번 수행한 다음에
    w_t = n//2
    m_t = m//1


    if m_t <= w_t:
        # 남자 만들 수 있는 만큼 만든다.
        team += m_t

        # 남은 여자 남자
        n -= (m_t * 2)
        m -= (m_t)
        
        collect_k = n+m
    else:
        # 여자 만들 수 있는 만큼 만든다.
        team += w_t

        # 남은 여자 남자
        n -= (w_t * 2)
        m -= (w_t)

        collect_k = n+m
       

    while collect_k<=k:
        if collect_k == k:
            break
        # 팀 1개 해체
        team -= 1
        n += 2
        m += 1
        # collect_k 업데이트 : m을 누적합 시키고 있기에 collect_k += (n+m)이 아니라, collect_k = n+m이다.
        collect_k = (n+m)

    return team

if __name__ == "__main__":
    print(solution())