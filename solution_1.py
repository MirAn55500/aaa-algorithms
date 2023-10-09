def validate_pushed_popped(pushed: list, popped: list) -> bool:
    stack = []
    popped.reverse()
    for elem in pushed:
        stack.append(elem)
        while stack and stack[-1] == popped[-1]:
            stack.pop()
            popped.pop()
    return len(popped) == 0


def solution():
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    result = validate_pushed_popped(pushed, popped)
    print(result)


solution()
