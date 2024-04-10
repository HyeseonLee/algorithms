import sys

# 스택을 활용하여 괄호 문자열이 올바른지 판단하는 함수
def is_valid_parenthesis(parentheses):
    stack = []
    for char in parentheses:
        if char == '(':
            stack.append(char)
        else:
            # 스택이 비어있거나 짝이 맞지 않는 경우
            if not stack or stack.pop() != '(':
                return "NO"
    # 모든 괄호를 확인한 후에도 스택이 비어있지 않은 경우
    if stack:
        return "NO"
    return "YES"

T = int(sys.stdin.readline().strip())

for _ in range(T):
    parentheses = sys.stdin.readline().strip()
    print(is_valid_parenthesis(parentheses))
