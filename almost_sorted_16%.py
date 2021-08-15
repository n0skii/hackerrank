#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'modifySequence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def binarySearch(arr, startAt, upto, elem):
    r = upto + 1
    l = startAt - 1
    while (r - l > 1):
        m = l + (r - l)//2
        if (arr[m] > elem):
            r = m
        else:
            l = m
    return r


def modifySequence(arr):
    n = len(arr)
    lasts = list()
    offset = 1
    lastInd = 0
    negOffset = 1

    lasts.append(1)
    if (arr[0] != 1):
        lasts.append(arr[0])
        lastInd += 1
        negOffset -= 1

    for i in range(1, n):
        elem = arr[i] - offset
        offset += 1
        if (elem > lasts[lastInd]):
            lastInd += 1
            lasts.append(elem)
            # print(lasts, offset)
        elif(elem < 1):
            continue
        else:
            if (elem == lasts[lastInd]):
                negOffset += 1
                continue
            else:
                indexToInsert = binarySearch(lasts, 0, lastInd, elem)
                lasts[indexToInsert] = elem

    return offset - lastInd - negOffset


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
