import sys

## 풀이 1 : deque 버전 O(m * nlogn)
from collections import deque

n,m = map(int, sys.stdin.readline().strip().split())
n_arr = deque(sorted(list(map(int, sys.stdin.readline().strip().split()))))
res = 0

for _ in range(m): # O(m * nlogn)
    num1 = n_arr.popleft()
    num2 = n_arr.popleft()
    new_card = num1+num2

    n_arr.append(new_card)
    n_arr.append(new_card)

    n_arr = deque(sorted(n_arr)) # O(nlogn)

print(sum(n_arr))

## 풀이 2 : heapq 버전 O(m * logn)
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
cards = [int(x) for x in sys.stdin.readline().split()]
# cards 리스트를 heap으로 변환
heapq.heapify(cards)

for _ in range(m): # O(m * logn)
    card1 = heapq.heappop(cards) #O(logn)
    card2 = heapq.heappop(cards) 

    heapq.heappush(cards, card1 + card2) #O(logn)
    heapq.heappush(cards, card1 + card2)

print(sum(cards))