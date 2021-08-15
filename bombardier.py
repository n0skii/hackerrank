#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#


def bomberMan(n, grid):
    normalGrid = list()
    for g in grid:
        subGrid = list()
        for i in range(len(g)):
            subGrid.append(3 if g[i] == 'O' else 0)
        normalGrid.append(subGrid)

    uniqueGrids = list()
    uniqueGrids.append(normalGrid)
    for i in range(1, 7):
        newGrid = uniqueGrids[-1].copy()
        for y in range(len(grid)):
            newGrid[y] = [elem - 1 for elem in newGrid[y]]
        if (i % 2 == 0):
            for y in range(len(grid)):
                newGrid[y] = [(3 if elem <= 0 else elem)
                              for elem in newGrid[y]]
        else:
            for y in range(len(grid)):
                for t in range(len(grid[0])):
                    if (newGrid[y][t] == 0):
                        if (y > 0 and newGrid[y - 1][t] != 0):
                            newGrid[y - 1][t] = -1
                        if (y < len(grid) - 1 and newGrid[y + 1][t] != 0):
                            newGrid[y + 1][t] = -1
                        if (t > 0 and newGrid[y][t - 1] != 0):
                            newGrid[y][t - 1] = -1
                        if (t < len(grid[0]) - 1 and newGrid[y][t + 1] != 0):
                            newGrid[y][t + 1] = -1
            for i in range(len(newGrid)):
                newGrid[i] = [(0 if elem == -1 else elem)
                              for elem in newGrid[i]]

        uniqueGrids.append(newGrid)

    index = n
    if (n < 3):
        index = n
    else:
        index = ((n + 1) % 4) + 3

    gridToReturn = ["".join([('.' if uniqueGrids[index][i][y] == 0 else 'O') for y in range(
        len(uniqueGrids[index][i]))]) for i in range(len(uniqueGrids[index]))]

    return gridToReturn


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
