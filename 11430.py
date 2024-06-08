import sys

def solution():
    n = int(sys.stdin.readline().strip())

    graph = []
    for i in range(n):
        li = list(map(int, sys.stdin.readline().strip().split()))
        graph.append(li)


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
    
    for item in graph:
        print(" ".join(map(str, item)))

if __name__ == "__main__":
    solution()