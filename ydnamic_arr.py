#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    arr = [list() for _ in range(n)]
    lastAns = 0
    ansArr = list()

    for q in queries:
        if q[0] == 1:
            arr[(q[1] ^ lastAns) % n].append(q[2])
        else:
            ind = (q[1] ^ lastAns) % n
            lastAns = arr[ind][q[2] % len(arr[ind])]
            ansArr.append(lastAns)

    return ansArr


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
