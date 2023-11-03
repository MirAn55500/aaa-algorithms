def count_zero_visitors_counters(N: int, M: int, university_segments: list) -> int:
    university_segments.sort()
    count = 0
    end = -1
    for i in range(M):
        l, r = university_segments[i]
        if l > end:
            count += (l - end - 1)
        end = max(end, r)
    count += (N - end - 1)
    return count


def solution():
    N, M = map(int, input().split())
    university_segments = []
    for i in range(M):
        b, e = map(int, input().split())
        university_segments.append([b, e])
    print(count_zero_visitors_counters(N, M, university_segments))


solution()
