#!/bin/python3

import math
import os
import random
import re
import sys
from typing import ByteString
from operator import itemgetter

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#


def intersect(a, b) -> bool:
    if (len(a[4].intersection(b[4])) == 0):
        return False
    return True

    # minDist = min(abs(a[0] - b[0]), abs(a[1] - b[1]))
    # maxDist = max(abs(a[0] - b[0]), abs(a[1] - b[1]))
    # if (minDist == 0):
    #     if (maxDist > a[2] + b[2]):
    #         return False
    #     else:
    #         return True
    # if ((minDist <= a[3] and maxDist <= b[3]) or (minDist <= b[3] and maxDist <= a[3])):
    #     return True
    # else:
    #     return False


def twoPluses(grid):
    dims = [len(grid), len(grid[0])]
    bestAreas = [0, 0]
    allCubes = list()

    for i in range(dims[0]):
        for y in range(dims[1]):
            if (grid[i][y] == 'B'):
                continue
            coords = set()
            coords.add(tuple([i, y]))
            cubes = 0
            allCubes.append([i, y, 0, 1, coords])
            iter = min([i, y, dims[0] - 1 - i, dims[1] - 1 - y])
            for it in range(1, iter + 1):
                if (grid[i + it][y] == 'B' or grid[i][y + it] == 'B'
                        or grid[i - it][y] == 'B' or grid[i][y - it] == 'B'):
                    break
                coords.add(tuple([i + it, y]))
                coords.add(tuple([i, y + it]))
                coords.add(tuple([i - it, y]))
                coords.add(tuple([i, y - it]))
                cubes += 1
                allCubes.append([i, y, cubes, 1 + cubes * 4, coords.copy()])

    allCubes = sorted(allCubes, key=itemgetter(3))

    if (len(allCubes) == 0 or len(allCubes) == 1):
        return 0

    maxDist = 0
    num = len(allCubes) - 1
    while(num > 0 and allCubes[num][3] * allCubes[num - 1][3] > maxDist):
        for i in reversed(range(num)):
            if (not intersect(allCubes[num], allCubes[i])):
                newDist = allCubes[num][3] * allCubes[i][3]
                if (maxDist < newDist):
                    maxDist = newDist
                break
        num -= 1

    return maxDist


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + "\n")

    fptr.close()
