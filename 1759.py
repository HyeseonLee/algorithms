import sys
sys.setrecursionlimit(10**6)

def solution():

    l,c = map(int, sys.stdin.readline().strip().split())
    c_arr = list(sys.stdin.readline().strip().split())
    c_arr.sort()
    answer = []

    moum = 'aeiou'
    jaum = 'bcdfghjklmnpqrstvwxyz'

    def is_okay(pw):
        moum_cnt = 0
        jaum_cnt = 0

        for char in pw:
            if char in moum:
                moum_cnt +=1
            elif char in jaum:
                jaum_cnt +=1

        if moum_cnt>=1 and jaum_cnt>=2:
            # print("통과", pw)
            return True
        else:
            # print("땡", pw)
            return False

    def password(start_idx, ans):
        #2. 종료 조건?
        if len(ans)==l:
            # password가 다 만들어 진 다음에 is_okay 검사하기
            if is_okay(ans):
                answer.append(ans[:])
            return
        
        #3. 갈 수 있는 곳 순회
        for i in range(start_idx,c):
            #4. 갈 수 있나?
            ans.append(c_arr[i])
            password(i+1,ans)
            ans.pop()

    password(0, [])
    for item in answer:
        print(''.join(map(str, item)))

    return None

if __name__=="__main__":
    solution()