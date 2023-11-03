def find_pairs(a: list, target: int) -> list:
    ans = []
    a.sort()
    for i in range(len(a)):
        if a[i] > target / 2:
            return ans
        for j in range(i+1, len(a)):
            if a[i] + a[j] == target:
                ans.append([a[i], a[j]])
    return ans


def solution():
    A = input()
    target = input()
    A = list(map(int, A.split(',')))
    target = int(target)
    print(str(find_pairs(A, target)))


solution()
