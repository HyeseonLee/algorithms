import sys

def solution():
    n = int(sys.stdin.readline().strip())
    level_arr = list(map(int, sys.stdin.readline().strip().split()))
    level_arr.sort()
    gold = 0
    level = 0

    while len(level_arr)>1:
        level = level_arr.pop()
        add_item = level_arr.pop()
        gold += (level+add_item)
        level_arr.append(level)

    return gold

if __name__ == "__main__":
    print(solution())