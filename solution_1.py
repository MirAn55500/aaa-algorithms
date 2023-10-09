def max_even_sum(numbers: list) -> int:
    numbers = sorted(numbers)
    summa = sum(numbers)
    if summa % 2 == 0:
        return summa
    else:
        for element in numbers:
            if element % 2 == 1:
                summa -= element
                return summa


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_even_sum(numbers)
    print(result)


solution()
