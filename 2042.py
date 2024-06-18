import sys


# 1. 세그먼트 트리 만들기
def build(tree, data, n):
    for i in range(n):
        tree[n+i] = data[i]
    for i in range(n-1, 0, -1):
        tree[i] = tree[i*2] + tree[i*2+1]

# 2. 구간합 쿼리
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

# 3. 업데이트 함수
def update(tree, n, index, value):
    index += n
    tree[index] = value
    while index > 1:
        index //= 2
        tree[index] = tree[index*2] + tree[index*2+1]

n,m,k = map(int, sys.stdin.readline().split())
data = []
result = []
tree = [0]*(2*n)

for _ in range(n):
    data.append(int(sys.stdin.readline().strip()))

build(tree,data,n)

for _ in range(m+k): # O( (m+k)*logN ) = O(10^4 * log10^6)
    a,b,c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(tree,n,b-1,c)
    elif a == 2:
        result.append(query(tree,n,b-1,c))

for r in result:
    print(r)