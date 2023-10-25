def max_even_sum(numbers: list) -> int:
    summ = sum(numbers)
    if summ % 2 == 0:
        return summ

    min_not_even = None
    for i in numbers:
        if i % 2 == 1 and min_not_even is None:
            min_not_even = i
        elif i % 2 == 1 and i < min_not_even:
            min_not_even = i

    return summ - min_not_even


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_even_sum(numbers)
    print(result)


solution()
