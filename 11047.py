import sys

def solution():
    # 1. 입력값 받고, 세팅
    res = 0
    n,k = map(int, sys.stdin.readline().strip().split())
    coin_arr = []
    for _ in range(n):
        v = int(sys.stdin.readline().strip())
        coin_arr.append(v)

    # 2. 자, 나는 K를 만들거에요. 제일 큰 동전부터 사용하려고 해요.
    while k>0:
        target = coin_arr.pop()
        
        if k//target > 0:
            res += k//target
            k = k%target
    
    return res

if __name__ == "__main__":
    print(solution())