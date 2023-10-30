def max_div3_sum(numbers: list) -> int:
    # numbers.sort()
    summa = sum(numbers)
    remain = summa % 3
    odd_elem_1 = None
    odd_elem_2 = []


    if remain == 0:
        return summa
    # если остаток 1, то ищем 2 числа с остатком 2
    # или 1 число с остатком 1, сравниваем
    # если остаток 2, то ищем 2 числа с остатком 1 или
    # 1 число с остатком 2, сравниваем
    for element in numbers:
        # поиск числа
        if element % 3 == remain and (odd_elem_1 is None or element < odd_elem_1):
            odd_elem_1 = element

        # поиск 2 чисел
        elif element % 3 == (3 - remain):
            odd_elem_2.append(element)
            odd_elem_2.sort()
            if len(odd_elem_2) > 2:
                odd_elem_2.pop()

    if sum(odd_elem_2) != 0 and odd_elem_1 is not None:
        summa -= min(odd_elem_1, sum(odd_elem_2))
    elif odd_elem_1 is None:
        summa -= sum(odd_elem_2)
    else:
        summa -= odd_elem_1
    return summa


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_div3_sum(numbers)
    print(result)


solution()
