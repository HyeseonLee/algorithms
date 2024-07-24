import sys

n,l = map(int, sys.stdin.readline().strip().split())

water = []
for _ in range(n):
    s,e = map(int, sys.stdin.readline().strip().split())
    water.append((s,e))
water.sort()

bridge = 0
pointer = 0

for s,e in water: # 10^4
    if s>pointer:
        pointer = s
    
    min_bridge_num = (e-pointer)//l
    bridge += min_bridge_num
    pointer += l*min_bridge_num


    while pointer < e:
        pointer += l
        bridge += 1

print(bridge)
