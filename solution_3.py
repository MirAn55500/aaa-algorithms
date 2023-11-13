import heapq


class StreamMedian:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_num(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]


def solution():
    n = int(input())
    stream = StreamMedian()
    for i in range(n):
        line = input().split()
        command = line[0]
        if command == "ADD":
            stream.add_num(int(line[1]))
        elif command == "FIND_MEDIAN":
            print(f'{stream.find_median():.1f}')


solution()
