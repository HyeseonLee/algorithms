from collections import deque
import sys

class Queue:
    def __init__(self, init=None):
        self.dq = deque(init) if init is not None else deque()
    def size(self):
        return len(self.dq)
    def empty(self):
        return not self.dq 
    
    def push(self, x):
        self.dq.append(x)
    def pop(self):
        if self.empty():
            return Exception("empty")
        else:
            return self.dq.popleft() # 가장 왼쪽에 있는 요소를 제거한다. O(1)
    def front(self):
        if self.empty():
            return Exception("empty")
        else:
            return self.dq[0]
    def sum_(self):
        return sum(self.dq) #O(N)
    def print_(self):
        return print(self.dq)


def calculate_time(bridge_length, weight, truck_weights):
    time = 0
    wait = Queue(truck_weights)
    bridge = Queue([0]*bridge_length)
    done = []

    def show():
        print("wait: ", end="") 
        wait.print_()
        print("bridge: ", end="")
        bridge.print_()
        #print("done : ",done)
        print("time : ", time)

    while sum(done) != sum(truck_weights):
    # 다 done에 가야 끝난다.

        if wait.size()>=1 and bridge.sum_() + wait.front() <= weight :
            print("bridge에 올라갑니다.")
            # bridge에 올라간 트럭 무게 합 + wait에서 기다리고 있는 첫번째 트럭 무게 합이 감당 가능 무게보다 작거나 같을 때
            # bridge에 wait.front() 넣기
            bridge.push(wait.pop())
            done.append(bridge.pop())
            time+=1
            show()
        elif wait.size() >=1 and bridge.sum_()-bridge.front()+wait.front() <= weight:
            # 무게가 초과 되어 bridge에 올라갈 수 없을 때 
            # 숫자가 맨 앞에 올 때까지 땡기기 & time +=1
            print("done으로 나가고, bridge에 하나 올리기")
            bridge.push(wait.pop())
            done.append(bridge.pop())
            time+=1
            show()
        else:
            print("bridge에 올라갈 수 없어요. bridge에 올라간 것들 한칸씩 옮깁니다.")
            bridge.push(0)
            done.append(bridge.pop())
            time+=1
            show()
    return time

if __name__ == "__main__":
    # calculate_time(bridge_length, weight, truck_weights)
    print("결과 : ",calculate_time(2, 10, [7, 4, 5, 6]))
    print(calculate_time(100, 100, [10]))
    print(calculate_time(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
