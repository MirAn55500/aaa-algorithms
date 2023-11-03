import math


def check_rotation(arr: list) -> int:
    left = 0
    right = len(arr) - 1
    middle = 0
    elem = arr[0]
    if arr[left] < arr[right]:
        return 0
    while left < right:
        middle = math.floor((left + right)/2)
        if arr[middle] > arr[0]:
            left = middle + 1
        else:
            right = middle - 1
    if left == 0:
        left = 1
    return left

def solution():

    arr = list(map(int, input().split()))
    i = check_rotation(arr)
    print(i)

solution()
