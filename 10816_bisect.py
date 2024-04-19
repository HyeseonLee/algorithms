# from bisect import bisect_left, bisect_right

# # [left_v, right_v] 범위 내에 있는 원소 개수 출력 함수
# def cnt_within_range (arr, left_v, right_v):
#     # 맨 좌측 인덱스
#     left_idx = bisect_left(arr, left_v)
#     # 맨 우측 인덱스
#     right_idx = bisect_right(arr, right_v)
#     print(f"left_idx {left_idx} right_idx {right_idx}")
#     return right_idx - left_idx

# # 리스트 생성
# arr = [6,3,2,10,10,10,-10,-10,7,3]
# arr.sort()
# # left_v, right_v을 같은 값으로 줌으로써 값이 9인 원소 개수 출력
# print(cnt_within_range(arr, 9, 9)) # 0
# print(cnt_within_range(arr, 10, 10))
# # [4, 7] 범위 내에 있는 원소 개수 출력
# print(cnt_within_range(arr, 4, 7)) # 6 # 0 , 6

# from bisect import bisect_left, bisect_right


import sys
from bisect import bisect_left, bisect_right

def solution():
    n = int(sys.stdin.readline().strip())
    n_arr = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    m_arr = list(map(int, sys.stdin.readline().strip().split()))
    #    n = 1
    #    n_arr = [1]
    #    m = 8
    #    m_arr = [10,9,-5,2,3,4,5,1]

    n_arr.sort()

    for item in m_arr:
        l = bisect_left(n_arr, item)
        r = bisect_right(n_arr, item)
        print(r-l, end=" ")

    return None
        
if __name__ == "__main__":
	solution()