import sys

def solution(): # O(nlogn)
    n = int(sys.stdin.readline().strip())
    x_arr = list(map(int, sys.stdin.readline().strip().split()))

    x_check_arr = set(x_arr)
    x_check_arr = sorted(x_check_arr) # O(nlogn) : 내장 메소드 sorted는 팀소트를 하고, 최악의 경우 O(nlogn)이다. 

    res_arr = [ 0 for _ in range(n)]


    # X' 찾기 위해 x_arr를 순회하면서 target으로 지정 -> x_check_arr를 이분탐색 -> 찾고자 하는 갯수 계산

    for i in range(n): # O(n)
        # 이분 탐색 위한 초기 범위값 지정    
        start, end = 0, len(x_check_arr)-1 # 인덱스로 할당
        
        while start<=end: # O(logn)
            mid = (start+end)//2 # 인덱스로 탐색 중
        
            if x_check_arr[mid] == x_arr[i]: # X' 업데이트
                res_arr[i] = mid # 일치하는 값의 인덱스 값이 찾고자하는 개수와 같다.

            if x_check_arr[mid] > x_arr[i]:
                end = mid-1
            else:
                start = mid+1

    res= ' '.join(map(str, res_arr)) # O(n) | join은 문자열을 합치기 때문에, list 내부 요소의 str화 필요

    return res


def solution_bisect():
    import bisect

    n = int(input())
    x_arr = list(map(int, sys.stdin.readline().strip()))

    sorted_arr = sorted(list(set(x_arr))) # O(nlogn)
    res_arr = []

    # O(nlogn)
    for x in x_arr: # O(n)
        count = bisect.bisect_left(sorted_arr, x) # O(nlogn) | x가 들어가게 될 인덱스 알려줌 = 이것 자체가 압축된 값을 의미
        res_arr.append(count)

    print(*res_arr)
	
def solution_hashmap():
    n = int(input())
    x_arr = list(map(int, sys.stdin.readline().strip()))

    sorted_arr = sorted(list(set(x_arr))) # O(nlogn)
    res_dic = {}

    # sorted_arr를 돌면서 딕셔너리에 값, idx 넣기
    for i in range(len(sorted_arr)): # O(n)
        res_dic[sorted_arr[i]] = i # O(1) | idx 자체가 그것보다 작은 수의 개수를 의미하기 때문 

    for i in x_arr:
        print(res_dic[i], end=" ") # res_dec[i(키값)]는 value를 나타낸다. 
	

if __name__ == "__main__":
    print(solution())
    