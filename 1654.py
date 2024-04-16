import sys

def solution():
    l = 0
    # k, n = map(int, sys.stdin.readline().strip().split())
    # k_arr = [
    #    int(sys.stdin.readline().strip())
    #    for _ in range(k)
    #]

    k,n = 1,3
    k_arr = [3]

    min_l, max_l = 1, max(k_arr) # O(K)

    while min_l <= max_l:
        # 중간 길이 계산
        mid = (min_l + max_l)//2

        # 몇개의 랜선이 생기는지 계산
        collected_line = 0
        for line in k_arr:
            collected_line += line // mid

        # 랜선 갯수의 총합이 >= N일 때, l = mid, 최대의 mid를 찾아야하기에 뒤에도 있는지 찾고 싶어서 min_l = mid+1
        if collected_line >= n:
            l = mid
            min_l = mid+1
        else:
            # 랜선 갯수 총합이 < N일 때, max_l = mid-1
            max_l = mid-1
        

    return l

if __name__ == "__main__":
    print(solution())