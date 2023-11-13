import heapq


def merge_k_sorted(arrs: list) -> list:
    heap = [(arr[0], i, 0) for i, arr in enumerate(arrs) if arr]
    heapq.heapify(heap)

    ans = []
    while heap:
        val, arr_idx, pos_idx = heapq.heappop(heap)
        ans.append(val)
        if pos_idx < len(arrs[arr_idx]) - 1:
            next_val = arrs[arr_idx][pos_idx + 1]
            print(heap)
            heapq.heappush(heap, (next_val, arr_idx, pos_idx + 1))
    return ans
#
#
# def read_multiline_input():   # удалить эту функцию
#     arrs = [[1, 2, 3, 4, 5, 6], [4, 5, 6, 8, 9], [2, 4, 7, 11]]
#     return arrs


def solution():
    arrs = read_multiline_input() # эта функция уже написана
    merged = merge_k_sorted(arrs)
    print(' '.join([str(el) for el in merged]))


solution()
