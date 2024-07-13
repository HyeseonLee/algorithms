import sys
# import random

# n,m =100000, 2000000000
# n_arr = [random.randint(0, 1000000000) for _ in range(100000)]
# n_arr = set(n_arr)
# n_arr = sorted(list(n_arr))


n,m = map(int, sys.stdin.readline().strip().split())

n_arr = []
for _ in range(n):
    n_arr.append(int(sys.stdin.readline().strip()))

n_arr = sorted(n_arr) # O(nlogn)

min_dif = float("inf")
left = 0
right = 1

while right < n:
    if left == right:
        right += 1
        continue
    
    dif = n_arr[right] - n_arr[left]

    if dif >= m:
        min_dif = min(min_dif, dif)
        left += 1
    else:
        right += 1

print(min_dif)

