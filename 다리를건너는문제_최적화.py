from collections import deque

class Queue:
    def __init__(self, init=None):
        # O(1)
        self.dq = deque(init) if init is not None else deque()
        self.total_weight = 0 
        
    def size(self):
        # O(1)
        return len(self.dq)
    
    def empty(self):
        # O(1)
        return not self.dq 
    
    def push(self, x):
        # O(1)
        self.dq.append(x)
        self.total_weight += x

    def pop(self):
        # O(1) (왜냐면, deque가 이중 연결리스트로 구현되어 있기 때문!)
        if self.empty():
            return Exception("empty")
        else:
            self.total_weight -= self.front()
            return self.dq.popleft() # 가장 왼쪽에 있는 요소를 제거한다. O(1)
    
    def front(self):
        # O(1)
        if self.empty():
            return Exception("empty")
        else:
            return self.dq[0]



def calculate_time(bridge_length, weight, truck_weights):
    time = 0
    wait = Queue(truck_weights)
    bridge = Queue([0]*bridge_length)
    done = []

    def done_append():
        if bridge.front() == 0:
            bridge.pop()
        else:
            done.append(bridge.pop())
    # def show():
    #     print("wait: ", end="") 
    #     wait.print_()
    #     print("bridge: ", end="")
    #     bridge.print_()
    #     print("done : ",done)
    #     print("time : ", time)

    while len(done) != len(truck_weights): # O(트럭의 개수 N) 모든 트럭이 다 건널 때까지 while문을 돈다.
        if wait.size()>=1 and bridge.total_weight + wait.front() <= weight : # bridge.sum_()이 O(bridge_length N)이기에, class 필드를 사용함으로써 O(1)연산으로 바꾸었다.
            bridge.push(wait.pop())
            done_append()
        elif wait.size() >=1 and bridge.total_weight-bridge.front()+wait.front() <= weight:
            bridge.push(wait.pop())
            done_append()
        else:
            bridge.push(0)
            done_append()           
        time+=1
        # show()
    return time

if __name__ == "__main__":
    print("결과 : ",calculate_time(2, 10, [7, 4, 5, 6]))
    print("결과 : ", calculate_time(100, 100, [10]))
    print("결과 : ", calculate_time(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
