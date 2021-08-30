#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def arrayManipulation(n, queries):
    start = list()
    end = list()
    toAdd = list()
    for q in queries:
        start.append(q[0] - 1)
        end.append(q[1])
        toAdd.append(q[2])

    numQ = len(queries)
    allInds = start + end
    lastInd = -1
    max = 0
    curSum = 0
    for ind in sorted(range(len(allInds)), key=allInds.__getitem__):
        index = allInds[ind]
        if lastInd != index:
            max = curSum if (max < curSum) else max
            lastInd = index
        adding = toAdd[ind] if ind < numQ else -toAdd[ind - numQ]
        curSum += adding

    return max


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + "\n")

    fptr.close()
