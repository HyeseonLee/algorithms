import sys

def solution():
    def make_arr(item, answer):
        #1. 체크인

        #2. 끝나야하나요?
        if len(answer)==m:
            ans.append(tuple(answer))
            return
            
        #3. 갈 수 있는 곳 순회
        for j in range(n):
            #4. 갈 수 있나?
            if not visited[j]:
                #5. 가쟈
                answer.append(num_arr[j])
                visited[j] = True
                make_arr(num_arr[j], answer)
                answer.pop()
                visited[j] = False

    n,m = map(int, sys.stdin.readline().strip().split())
    num_arr = sorted(list(map(int, sys.stdin.readline().strip().split())))

    visited = [False]*n
    ans = []
    make_arr(num_arr[0], [])

    ans = sorted(list(set(ans)))

    for item in ans:
        print(*item)
    
    return None

if __name__ == "__main__":
    solution()