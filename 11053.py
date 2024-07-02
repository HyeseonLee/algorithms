import sys
from bisect import bisect_left

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

lis = []

for num in arr:
    # num이 들어갈 수 있는 pos 탐색
    pos = bisect_left(lis,num)

    # 만약 pos가 len(lis)보다 작다면 그 pos 값 변경 필요
    if pos < len(lis):
        lis[pos] = num
    else:
        lis.append(num)

print(len(lis))