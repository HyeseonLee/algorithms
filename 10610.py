import sys

    
def solution():
    num = sys.stdin.readline().strip()
    num_arr = [int(num) for num in num]
    num_arr.sort(reverse=True) #O(5)

    if 0 not in num_arr:
        return -1
    
    if sum(num_arr)%3 == 0:
        return ''.join(map(str, num_arr))
    else:
        return -1

if __name__ == "__main__":
    print(solution())