def knapsack(values: list, weights: list, capacity: int):
    a = [[0 for _ in range(capacity + 1)] for _ in range(len(values) + 1)]
    for i in range(1, len(values) + 1):
        for j in range(1, capacity+1):
            if i == 1 and j >= weights[0]:
                a[i][j] = values[i-1]
            elif j >= weights[i-1]:
                a[i][j] = max(a[i-1][j], values[i-1] + a[i-1][j-weights[i-1]])
            else:
                a[i][j] = a[i - 1][j]
    return a[-1][-1]


def solution():
    values = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    capacity = int(input())
    print(knapsack(values, weights, capacity))

solution()