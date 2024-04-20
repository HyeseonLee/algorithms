import sys
from collections import Counter

def solution(): # O(m+n)
    n = int(sys.stdin.readline().strip())
    n_arr = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    m_arr = list(map(int, sys.stdin.readline().strip().split()))

#    n = 5
#    n_arr = [4,1,5,2,3]
#    m=5
#    m_arr=[1,3,7,9,5]

    counter = Counter(n_arr) # O(n)
    
    for item in m_arr: # O(m)
        value = counter[item]
        print(0 if value==0 else 1)

    return None

if __name__ == "__main__":
    solution()


# 해시맵 솔루션
def solution2(): # O(n+m)
    n = int(sys.stdin.readline().strip())
    n_arr = set(map(int, sys.stdin.readline().strip().split())) # O(n)
    m = int(sys.stdin.readline().strip())
    m_arr = list(map(int, sys.stdin.readline().strip().split())) # O(m)

    for item in m_arr: # O(m)
        print(1 if item in n_arr else 0) # O(1)
    
    return None