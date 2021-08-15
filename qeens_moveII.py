#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#


def queensAttack(n, k, y, x, obstacles):
    n -= 1
    y -= 1
    x -= 1
    # up, right, down, left
    spaceArr = sortedDist = [n - y, n - x, y, x]
    sortedDist.sort()

    adjacent = False
    # cachedInd = -1, anotherCachedInd = -1
    for i, s in enumerate(spaceArr):
        if s == sortedDist[1]:
            cachedInd = i
        if s == sortedDist[0]:
            anotherCachedInd = i

    if abs(cachedInd - anotherCachedInd) != 2:
        adjacent = True

    allPossibleMoves = 0
    for i, dist in enumerate(sortedDist):
        if i == 0:
            allPossibleMoves += dist * 3
            continue
        if adjacent:
            if i == 3:
                allPossibleMoves += dist
            else:
                allPossibleMoves += 2 * dist
        else:
            if i == 1:
                allPossibleMoves += dist * 3
            else:
                allPossibleMoves += dist

    reductionArr = [0 for _ in range(8)]
    difference = y - x
    coordSum = y + x
    for obstacle in obstacles:
        oy = obstacle[0] - 1
        ox = obstacle[1] - 1

        if ox == x:
            if oy < y:
                reduction = oy + 1
                if reduction > reductionArr[0]:
                    reductionArr[0] = reduction
                continue
            else:
                reduction = n - oy + 1
                if reduction > reductionArr[1]:
                    reductionArr[1] = reduction
                continue
        if oy == y:
            if ox < x:
                reduction = ox + 1
                if reduction > reductionArr[2]:
                    reductionArr[2] = reduction
                continue
            else:
                reduction = n - ox + 1
                if reduction > reductionArr[3]:
                    reductionArr[3] = reduction
                continue

        if oy + ox == coordSum:
            print("DIAGONAL")
            if ox > x:
                reduction = int(min(n - ox, oy)) + 1
                if reduction > reductionArr[4]:
                    reductionArr[4] = reduction
                continue
            else:
                reduction = int(min(ox, n - oy)) + 1
                if reduction > reductionArr[5]:
                    reductionArr[5] = reduction
                continue
        if oy - ox == difference:
            print("DIAG")
            if ox > x:
                reduction = n - max(oy, ox) + 1
                if reduction > reductionArr[6]:
                    reductionArr[6] = reduction
                continue
            else:
                reduction = min(oy, ox) + 1
                if reduction > reductionArr[7]:
                    reductionArr[7] = reduction
                continue

    for reduction in reductionArr:
        allPossibleMoves -= reduction

    print(reductionArr)
    return allPossibleMoves


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + "\n")

    fptr.close()
