def calculate_stock_spans(prices: list) -> list:
    n = len(prices)
    curr_mass = []
    ans = []
    for i, price in enumerate(prices):
        print(curr_mass, price, ans)
        while curr_mass and prices[curr_mass[-1]] <= price:
            curr_mass.pop()

        if not curr_mass:
            ans.append(i + 1)
        else:
            ans.append(i - curr_mass[-1])

        curr_mass.append(i)
    return ans


def solution():
    prices = list(map(int, input().split()))
    spans = calculate_stock_spans(prices)
    print(' '.join(map(str, spans)))


solution()
