#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestIncreasingSubsequence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def binarySearch(arr, startAt, upto, elem):
    r = upto
    l = startAt
    while (r - l > 1):
        m = l + (r - l)//2
        if (arr[m] >= elem):
            r = m
        else:
            l = m
    return r - 1


def longestIncreasingSubsequence(arr):
    n = len(arr)
    lengths = [0 for _ in range(n)]
    lasts = [float('inf') for _ in range(n)]

    lengths[0] = 1
    lasts[0] = arr[0]
    largestSeq = 1
    for i in range(1, n):
        # print(lasts)

        if (arr[i] < lasts[0]):
            lasts[0] = arr[i]
        elif (arr[i] > lasts[largestSeq - 1]):
            lasts[largestSeq] = arr[i]
            largestSeq += 1
            lengths[largestSeq - 1] = largestSeq
        else:
            if (arr[i] == lasts[largestSeq - 1]):
                continue

            indToInsert = binarySearch(lasts, -1, largestSeq, arr[i])
            # Commented out for inoptimality
            # print(indToInsert)
            # if (lasts[indToInsert] == arr[i] or arr[i] == lasts[0] or
            #         arr[i] == lasts[largestSeq - 1]):
            #     continue
            # else:
            lasts[indToInsert + 1] = arr[i]

    return largestSeq


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
