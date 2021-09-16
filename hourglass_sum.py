#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    _max = float("-inf")
    for i in range(1, 5):
        for y in range(1, 5):
            newSum = (
                arr[i - 1][y - 1]
                + arr[i - 1][y]
                + arr[i - 1][y + 1]
                + arr[i][y]
                + arr[i + 1][y - 1]
                + arr[i + 1][y]
                + arr[i + 1][y + 1]
            )
            if newSum > _max:
                _max = newSum
    return _max


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
