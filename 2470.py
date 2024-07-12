import sys

n = int(sys.stdin.readline().strip())
n_arr = list(map(int, sys.stdin.readline().strip().split()))
n_arr.sort() # O(N)

min_dif = abs(0-float("inf"))
item1 = 0
item2 = 0

left = 0
right = len(n_arr)-1

while left<right: # O(N)
    sum = n_arr[left] + n_arr[right]

    # 0과 제일 가까운 값을 만드는 상황으로 업데이트 진행
    if abs(sum)<min_dif:
        item1 = n_arr[left]
        item2 = n_arr[right]
        min_dif = abs(sum)

        # 딱 0인 경우는 그냥 바로 프로그램 종료할 수 있도록 break !
        if sum == 0:
            break
    
    # 투 포인터 범위 이동
    if sum>0:
        right -= 1
    else:
        left += 1

print(min(item1, item2), max(item1, item2))