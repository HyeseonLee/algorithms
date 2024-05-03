import sys

def solution():
    n, m, k = map(int, sys.stdin.readline().strip().split())
    
    # 최대 팀 수를 구하는 초기 로직
    max_teams = min(n // 2, m)
    remaining_students = n + m - 3 * max_teams

    # 인턴쉽에 필요한 학생 수가 남은 학생보다 많은 경우, 팀을 해체
    while remaining_students < k and max_teams > 0:
        max_teams -= 1
        remaining_students += 3

    return max_teams

if __name__ == "__main__":
    print(solution())
