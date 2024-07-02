import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
inc_count = [1]*n
dec_count = [1]*n

for i in range(1, len(arr)):
    if arr[i] >= arr[i-1]:
        inc_count[i] = inc_count[i-1] + 1
    if arr[i] <= arr[i-1]:
        dec_count[i] = dec_count[i-1] + 1

print(max(max(inc_count), max(dec_count)))