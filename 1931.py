import sys

def solution():
    n = int(sys.stdin.readline().strip())
    waiting = []
    count = 0
    time = 0
    for _ in range(n):
        s, e = map(int, sys.stdin.readline().strip().split())
        waiting.append([s,e])

    waiting.sort(key=lambda x : [x[1],x[0]], reverse=True)


    while waiting:
        item = waiting.pop()      
        if time <= item[0]:
            count += 1
            time = item[1]

    return count

if __name__ == "__main__":
    print(solution())