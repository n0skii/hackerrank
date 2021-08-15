#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Pattern

#
# Complete the 'angryChildren' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY packets
#


def angryChildren(k, packets):
    packets.sort()

    initialArr = packets[:k]
    currentSum = 0
    overallSum = 0
    for i, elem in enumerate(initialArr):
        currentSum += (2 * i - k + 1) * elem
        overallSum += elem
    
    minSum = currentSum
    for i in range(len(packets) - k):
        currentSum += (k - 1) * packets[i]
        overallSum -= packets[i]
        currentSum -= 2 * overallSum
        currentSum += (k - 1) * packets[i + k]
        overallSum += packets[i + k]

        minSum = currentSum if currentSum < minSum else minSum

    return minSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    packets = []

    for _ in range(n):
        packets_item = int(input().strip())
        packets.append(packets_item)

    result = angryChildren(k, packets)

    fptr.write(str(result) + '\n')

    fptr.close()
