import sys
import heapq

n,s = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
res = []

def two_pointer(n, arr, s, res):
    left = 0
    cur_sum = 0

    for right in range(n):
        cur_sum += arr[right]

        if cur_sum >= s:
            heapq.heappush(res, right-left+1)
            
        while cur_sum >= s and left <= right:
            cur_sum -= arr[left]
            heapq.heappush(res, right-left+1)

            left += 1
            # print("while", "cur_sum", cur_sum, "left", left, "right", right)

two_pointer(n, arr, s, res)

if not res:
    print(0)
else:
    print(res[0])
