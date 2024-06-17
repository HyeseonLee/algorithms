import sys

n,m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

def query(tree, n, left, right):
    result = 0
    left += n 
    right += n  
    
    while left < right:
        if left % 2:
            result += tree[left]
            left += 1
        if right % 2:
            right -= 1
            result += tree[right]
        left //= 2
        right //= 2
    
    return result

res = []        

# 세그먼트 트리 사용 : O(logN)
# 1.세그먼트 트리 만들기
tree = [0]*(2*n)

for i in range(n):
    tree[n+i] = data[i]
for i in range(n-1, 0, -1):
    tree[i] = tree[i*2] + tree[i*2+1]

for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())

    # 2.구간합 구하기
    res.append(query(tree,n,i-1,j))
    
for r in res:
    print(r)
