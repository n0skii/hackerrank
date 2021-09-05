#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#


# def twoStacks(maxSum, a, b):
#     bLen = len(b)
#     bInd = -1
#     maxNum = float("-inf")
#     startInd = 0

#     aSum = 0
#     for i in range(len(a)):
#         aSum += a[i]
#         if aSum <= maxSum:
#             startInd = i
#         else:
#             aSum -= a[i]

#     overallSum = aSum
#     for i in reversed(range(-1, startInd + 1)):
#         temp = overallSum
#         bIndTemp = bInd
#         while temp <= maxSum:
#             overallSum = temp
#             bInd = bIndTemp
#             maxNum = maxNum if (bInd + i + 2) <= maxNum else (bInd + i + 2)

#             if bIndTemp < bLen - 1:
#                 bIndTemp += 1
#             temp += b[bIndTemp]

#         if i == -1 or bInd == bLen - 1:
#             break

#         overallSum -= a[i]

#     return maxNum


def twoStacks(maxSum, a, b):
    a.reverse()
    b.reverse()
    stack, total, score = [], 0, 0

    while a:
        item = a.pop()
        if (total + item) <= maxSum:
            total += item
            score += 1
            stack.append(item)
        else:
            break

    maxScore = score

    while b:
        item = b.pop()
        total += item
        score += 1
        while total > maxSum and stack:
            total -= stack.pop()
            score -= 1
        if total <= maxSum and score > maxScore:
            maxScore = score

    return maxScore


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + "\n")

    fptr.close()
