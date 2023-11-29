def zero_sum_subarrays(arr: list) -> int:
    prefix_sum = 0
    sum_count = {0: 1}
    count = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum in sum_count:
            count += sum_count[prefix_sum]
            sum_count[prefix_sum] += 1
        else:
            sum_count[prefix_sum] = 1

    return count

def solution():
    arr = list(map(int, input().split()))
    count = zero_sum_subarrays(arr)
    print(count)

solution()
