# def solution():


# if __name__ == "__main__":
#     print(solution())

import sys
import heapq
from collections import deque


def solution():


    # n,m = map(int, sys.stdin.readline().strip().split())
    # pri_arr = list(map(int, sys.stdin.readline().strip().split()))
    n,m = 4,2
    pri_arr = [1,2,3,4]

    # 최초의 프린터 상태 - FIFO
    # priority 최댓값 구하기
    # 프린터 맨 처음 것의 priority가 최댓값이라면 -> pop & 출력횟수++ / 아니라면 pop해서 맨뒤에 push
    # m번째 놓여있는 것이 pop 될 때 까지

    # 엥 그러면 while 프린터에 아무것도 없을 때까지인가? 아니면 pop된게 m번재꺼일 때까지인가?

    count = 0

    # 최초의 프린터 만들기
    printer = deque()
    lst = [
        (idx, pri)
        for idx, pri in enumerate(pri_arr, start=0)
    ]
    for item in lst:
        printer.append(item)
    
    # 우선순위 최댓값을 위한 세팅
    pq = []
    for item in lst:
        idx, pri = item
        heapq.heappush(pq, (-pri, idx))

    # 프린터에 아무것도 없을 때까지
    while printer:
        # 맨 왼쪽꺼 priority가 나갈 차례인지 확인
        pop_idx, pop_pri = printer[0]
        print("pop_idx", pop_idx, "pop_pri", pop_pri)
        if pop_pri == -(pq[0][0]):
            # 나갈 차례임
            printer.popleft()
            heapq.heappop(pq)[0]
            count += 1
            if pop_idx == m:
                # 내가 알고 싶은 문서가 출력되었다. while문 종료 
                break
        else:
            # 나갈 차례가 아닙니다
            printer.append(printer.popleft())
    return count

if __name__ == "__main__" :
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        print(solution())