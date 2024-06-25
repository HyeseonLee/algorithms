import sys
from collections import deque

n = int(sys.stdin.readline().strip())
neg = deque()
pos = deque()
zero = []
one = []
res_arr = []

for _ in range(n): # O(n)
    num = int(sys.stdin.readline().strip())
    if num<0: neg.append(num)
    elif num==0: zero.append(num)
    elif num>1: pos.append(num)
    elif num==1: one.append(num)

neg = deque(sorted(neg)) # O(nlogn)
while len(neg)>1: # O(n)
    res_arr.append(neg.popleft()*neg.popleft())
if neg: # neg가 1개 남아있음
    if zero: # 0이 있다면, 0이랑 곱해서 무효화시키기
        res_arr.append(neg.popleft()*zero.pop()) # neg.popleft()
    else:
        res_arr.append(neg.popleft())

pos = deque(sorted(pos, reverse=True)) # O(nlogn)
while len(pos)>1: # O(n)
    res_arr.append(pos.popleft()*pos.popleft())
if pos:
    res_arr.append(pos.popleft())

while one: # O(n)
    res_arr.append(one.pop())

print(sum(res_arr)) # O(n)