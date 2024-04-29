import sys

def solution():
    n = int(sys.stdin.readline().strip())
    time = list(map(int, sys.stdin.readline().strip().split()))
    time.sort()
    result = [0]*(n)

    result[0] = time[0]
    for i in range(1,n):
        result[i] = result[i-1] + time[i]
        
    return sum(result)

if __name__ == "__main__":
    print(solution())