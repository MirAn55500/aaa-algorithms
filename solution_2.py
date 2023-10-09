def max_div3_sum(numbers: list) -> int:
    numbers.sort()
    summa = sum(numbers)
    remain1 = -1
    remain2 = [0]   # 0, чтобы сумма посчиталась

    if summa % 3 == 0:
        return summa
    # если остаток 1, то ищем 2 числа с остатком 2
    # или 1 число с остатком 1, сравниваем
    elif summa % 3 == 1:
        for element in numbers:
            if element % 3 == 1 and remain1 == -1:
                remain1 = element
            elif element % 3 == 2 and len(remain2) != 3:
                remain2.append(element)
            if remain1 != -1 and len(remain2) == 3:
                if sum(remain2) > remain1:
                    summa -= remain1
                else:
                    summa -= sum(remain2)
                return summa
        if remain1 != -1:
            summa -= remain1
        else:
            summa -= sum(remain2)
        return summa
    # если остаток 2, то ищем 2 числа с остатком 1 или
    # 1 число с остатком 2, сравниваем
    else:
        for element in numbers:
            if element % 3 == 2 and remain1 == -1:
                remain1 = element
            elif element % 3 == 1 and len(remain2) != 3:
                remain2.append(element)
            if remain1 != -1 and len(remain2) == 3:
                if sum(remain2) > remain1:
                    summa -= remain1
                else:
                    summa -= sum(remain2)
                return summa
        if remain1 != -1:
            summa -= remain1
        else:
            summa -= sum(remain2)
        return summa


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_div3_sum(numbers)
    print(result)


solution()
