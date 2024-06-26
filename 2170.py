import sys
from collections import deque

n = int(sys.stdin.readline().strip())
res = 0

# 처음에 점 하나 추가
lines = deque()

# 최초 선 긋기
x,y = map(int, sys.stdin.readline().strip().split())
lines.append((x,y))

for _ in range(n-1):
    x,y = map(int, sys.stdin.readline().strip().split())
    is_new_line = False

    for i in range(len(lines)):
        s,e = lines[i] # 맨 앞에 있는 것 빼기
        # print("here", s, e)
        if e<=x or y<=s:
            is_new_line = True
            # print("True")
        else: # 겹친다
            is_new_line = False
            lines[i] = (min(s,x), max(e,y))

        # print(lines)

    if is_new_line:
        lines.append((x,y))
    
    # print("lines", lines)



for line in lines:
    res += line[1] - line[0]
    # if line[1] >= 0 and line[0] <=0: # 음수, 양수에 있음
    #     res += abs(line[1]) + abs(line[0])
    # else:
    #     res += abs(abs(line[1])-abs(line[0]))

print(res)

# import sys

# segments = []
    
# n = int(sys.stdin.readline().strip())
# for _ in range(n):
#     x,y = map(int, sys.stdin.readline().strip().split())
#     segments.append((x, y))


# # 선분을 시작점 기준으로 정렬
# segments.sort()
    
# total_length = 0
# current_start, current_end = segments[0]

# for start, end in segments[1:]:
#     if start <= current_end:  # 현재 선분이 이전 선분과 겹치거나 인접해 있는 경우
#         current_end = max(current_end, end)  # 끝점을 확장합니다.
#     else:  # 현재 선분이 이전 선분과 겹치지 않는 경우
#         total_length += current_end - current_start  # 이전 선분의 길이를 추가합니다.
#         current_start, current_end = start, end  # 새로운 선분을 시작합니다.

# # 마지막 선분의 길이를 추가합니다.
# total_length += current_end - current_start
    
# print(total_length)



