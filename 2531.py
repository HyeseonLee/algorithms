import sys
import heapq

n,d,k,c = map(int, sys.stdin.readline().strip().split())
dishes = []
for _ in range(n):
    dishes.append(int(sys.stdin.readline().strip()))
dishes += dishes[:k-1]

res = []
for left in range(n):
    right = left+k
    k_arr = set(dishes[left:right])
    k_arr.add(c)
    heapq.heappush(res, -len(k_arr))

print(-res[0])        