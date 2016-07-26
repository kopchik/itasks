#!/usr/bin/env python3

"""
Not the most efficient algorithm in terms of memory :(
"""


def msort(l):
    length = len(l)
    if length <= 1:
        return l
    result = []
    left = msort(l[:length // 2])
    right = msort(l[length // 2:])
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

if __name__ == '__main__':
    tests = ([3, 2, 1], [], [1], [1, 2], [0, -3, 0])
    for t in tests:
        assert msort(t) == sorted(t)
