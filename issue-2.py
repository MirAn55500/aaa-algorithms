def rob_corovans(values: list):
    a = [0 for _ in range(len(values))]
    for i in range(len(values)):
        if i == 0:
            a[i] = values[0]
        elif i == 1:
            a[i] = max(values[:2])
        else:
            a[i] = max(a[i-2] + values[i], a[i-1])
    return a[-1]

def solution():
    values = list(map(int, input().split()))
    print(rob_corovans(values))

solution()