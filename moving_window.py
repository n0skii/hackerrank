#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#


# def solve(arr, queries):
#     _returns = list()
#     size = len(arr)
#     for q in queries:
#         globArr = list(arr[:q])
#         list.sort(globArr)
#         initialmax = globArr[-1]

#         start = 0
#         while start + q <= size - 1:
#             bisect.insort(globArr, arr[start + q])
#             del globArr[bisect.bisect_left(globArr, arr[start])]

#             newmax = globArr[-1]
#             if newmax < initialmax:
#                 initialmax = newmax
#             start += 1
#         _returns.append(initialmax)
#     return _returns


def Helper(arr, d):
    maximum = minimum = max(arr[:d])
    for i in range(d, len(arr)):
        if arr[i - d] == maximum:
            newMaximum = max(arr[i - d + 1 : i + 1])
        else:
            newMaximum = max(maximum, arr[i])
        minimum = min(minimum, newMaximum)
        maximum = newMaximum
    return minimum


def solve(arr, queries):
    result = []
    for ele in queries:
        result.append(Helper(arr, ele))
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
