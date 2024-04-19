import sys
from collections import Counter

def solution():
    n = int(sys.stdin.readline().strip())
    n_arr = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    m_arr = list(map(int, sys.stdin.readline().strip().split()))
    
    # n = 1
    # n_arr = [1]
    # m = 8
    # m_arr = [10,9,-5,2,3,4,5,1]

    counter = Counter(n_arr) # O(n)

    res = []
    for item in m_arr: # O(m)
        value = counter[item]
        res.append(value)
    
    return res

if __name__ == "__main__":
    answer = solution()
    print(*answer)