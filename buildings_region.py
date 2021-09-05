#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#


def findMin(arr, start, end):
    _min = float("inf")
    ind = -1
    for i in range(start, end):
        if arr[i] < _min:
            _min = arr[i]
            ind = i
    return _min, ind


def findLargest(arr, start, end):
    if end - start == 1:
        return arr[start]
    else:
        _min, ind = findMin(arr, start, end)
        region = (end - start) * _min
        if ind != start:
            temp = findLargest(arr, start, ind)
            region = temp if temp > region else region
        if ind != end - 1:
            temp = findLargest(arr, ind + 1, end)
            region = temp if temp > region else region

        return region


def largestRectangle(h):
    return findLargest(h, 0, len(h))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + "\n")

    fptr.close()
