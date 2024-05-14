import sys

def solution():
    n,m = map(int, sys.stdin.readline().strip().split())
    num_arr = [i for i in range(1,n+1)]
    visited = [False]*n
    answer = []


    def make(ans):
        #1. 체크인
        #2. 종료 조건 충족?
        if len(ans) == m:
            answer.append(tuple(ans))
            return
        #3. 갈 수 있는 곳 모두 순회
        for i in range(n):
            #4. 갈 수 있나?
            # if not visited[i]: # 이 문제에서는 이것이 필요 없다! 
                #5. 가자
                ans.append(num_arr[i])
                visited[i] = True
                make(ans)
                ans.pop()
                visited[i] = False

    # 가능한 모든 수열을 만들거에요. 
    make([])

    # 중복 제거
    answer = list(sorted(set(answer)))

    for a in answer:
        print(*a)

    return None

if __name__ == "__main__":
    solution(),