import sys
MOD_NUM = 1000000007

# 1. 세그먼트 트리 만들기
def build(tree,n,data):
    # 리프노드
    for i in range(n):
        tree[n+i] = data[i]
    # 내부노드 : 구간 곱 !
    for i in range(n-1,0,-1):
        tree[i] = (tree[2*i] * tree[2*i+1]) % MOD_NUM

# 2. 구간 곱
def query(tree,n,left,right):
    # left, right 인덱스를 트리에 맞게 조정
    left += n
    right += n
    result = 1 # 0?

    while left<right:
        if left%2:
            result *= tree[left] % MOD_NUM
            left += 1
        if right%2:
            right -= 1
            result *= tree[right] % MOD_NUM
        left //= 2
        right //=2

    return result % MOD_NUM

def update(tree,n,index,value):
    # index를 트리에 맞게 조정
    index += n

    # 업데이트
    tree[index] = value
    # 업데이트 전파
    while index>1:
        index //= 2
        tree[index] = ( tree[index*2] * tree[index*2+1] ) % MOD_NUM


n,m,k = map(int, sys.stdin.readline().strip().split())
data = []
tree = [0] * (2*n)
res = []
for _ in range(n):
    data.append(int(sys.stdin.readline().strip()))

build(tree,n,data)    

for _ in range(m+k):
    a,b,c = map(int, sys.stdin.readline().strip().split())
    if a==1:
        update(tree,n,b-1,c)
    elif a==2:
        res.append(query(tree,n,b-1,c))
        
for r in res:
    print(r)
