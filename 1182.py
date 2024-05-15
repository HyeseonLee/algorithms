import sys

def solution():
    def make(idx, ans, leng, cnt):
        #2. 종료 조건?
        if len(ans) == leng:
            # leng짜리 부분 수열 만들었습니다. sum이 s와 같은지 확인하시죠
            answer.append(ans[:]) # ⭐⭐⭐ ans는 참조형 데이터타입이고, make 함수 내에서 계속 바뀌니까 복사해서 넣어야함 !!!
            # sum이 s와 같든지 말든지 return ! 하나의 ans 완전체를 만들었으니 끝 !
            return        

        #3. 갈 수 있는 곳 모두 순회
        for i in range(idx,n): #O(n)
            #4. 갈 수 있나?
            if not visited[i]:
                #5. 가자
                ans.append(n_arr[i])
                visited[i] = True
                make(i+1, ans, leng, cnt)
                ans.pop()
                visited[i] = False

    n,s = map(int, sys.stdin.readline().strip().split())
    n_arr = list(map(int, sys.stdin.readline().strip().split()))

    cnt = 0
    answer = []
    
    # 부분 수열 만들기 : 길이가 1부터 n까지 있습니당 : O(n)
    for leng in range(1,n+1): 
        visited = [False]*n
        make(0, [], leng, cnt)

    # 결과 계산하기 : O(n)
    for item in answer: 
        if sum(item)==s:
            cnt += 1
    
    return cnt

if __name__ == "__main__":
    print(solution())