def two_sum(arr: list, k: int):
    index_dict = {}
    for i, num in enumerate(arr):
        num2 = k - num
        if num2 in index_dict:
            return index_dict[num2], i

        index_dict[num] = i
    return None


def solution():
    arr = list(map(int, input().split()))
    k = int(input())
    a, b = two_sum(arr, k)
    print(a, b)

solution()
