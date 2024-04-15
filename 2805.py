import sys
import heapq

def find_highest_hight():
    _, goal = map(int, sys.stdin.readline().strip().split())
    wood_arr = list(map(int, sys.stdin.readline().strip().split()))
    hight = 0



    # 가능한 H 최소, 최댓값 구하기
    ### 근데 .. 꼭 필요하진 않지만 있으면 좋나?
    # wood_arr의 최솟값/최댓값이 min_h, max_h
    max_pq = []
    for wood in wood_arr: #O(logN)
        heapq.heappush(max_pq, -wood) 
    min_h, max_h = 0, -max_pq[0]

    while min_h <= max_h: # O(logN)
        mid = (min_h + max_h) // 2

        # 얻을 수 있는 나무 양 계산
        collected_wood = 0
        for wood in wood_arr: # O(N)
            can_get = wood - mid
            if can_get>0:
                collected_wood += can_get         
        # print("모을 수 있는 나무", collected_wood) 
          
        if collected_wood >= goal:
            # 목표하는 나무 양을 채웠을 때 hight 업데이트 
            hight = mid
            min_h = mid + 1 # 최대의 hight를 만들어야하니까 계속 탐색
        else:
            max_h = mid-1        

    return hight

if __name__ == "__main__" :
    print(find_highest_hight())