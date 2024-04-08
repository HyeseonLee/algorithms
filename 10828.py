import sys 
stack = []

def push(item):
    stack.append(item)
def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()
def size():
    return len(stack)
def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]
def empty():
    return 1 if len(stack) == 0 else 0

num = int(sys.stdin.readline())

for _ in range(num):
    command = sys.stdin.readline().split()

    if command[0]=="push":
        push(command[1])
    elif command[0]=="pop":
        print(pop())
    elif command[0]=="size":
        print(size())
    elif command[0]=="empty":
        print(empty())
    elif command[0]=="top":
        print(top())