#!/bin/python3

from abc import abstractproperty
import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#


def matrixRotation(matrix, r):
    x = len(matrix[0])
    y = len(matrix)
    num_circles = int(min(x, y) / 2)
    flat_circles = list()
    flat_sides_len = list()
    for i in range(num_circles):
        circle = matrix[i][i : x - i]
        flat_sides_len.append(len(circle))
        circle += [m[x - 1 - i] for m in matrix[i + 1 : -i - 1]]
        circle += matrix[y - 1 - i][i : x - i][::-1]
        circle += [m[i] for m in matrix[i + 1 : -i - 1]][::-1]
        flat_circles.append(circle)

    curInd = [1 for _ in range(len(flat_circles))]
    for i, circle in enumerate(flat_circles):
        cLen = len(circle)
        indexes = [(i + (r % cLen)) % cLen for i in range(cLen)]
        flat_circles[i] = [circle[indexes[i]] for i in range(len(indexes))]

        rowToPrint = []
        for t in range(i):
            rowToPrint += [flat_circles[t][-curInd[t]]]

        rowToPrint += flat_circles[i][: flat_sides_len[i]]

        for t in reversed(range(i)):
            rowToPrint += [flat_circles[t][flat_sides_len[t] - 1 + curInd[t]]]
            curInd[t] += 1

        print(*rowToPrint, sep=" ")

    if x < y:
        for i in range(y - x):
            rowToPrint = []
            for t in range(len(flat_circles)):
                rowToPrint += [flat_circles[t][-curInd[t]]]

            for t in reversed(range(len(flat_circles))):
                rowToPrint += [flat_circles[t][flat_sides_len[t] - 1 + curInd[t]]]
                curInd[t] += 1

            print(*rowToPrint, sep=" ")

    for i in reversed(range(len(flat_circles))):
        rowToPrint = []
        for y in range(i):
            rowToPrint += [flat_circles[y][-curInd[y]]]

        rowToPrint += flat_circles[i][
            flat_sides_len[i] - 1 + curInd[i] : 2 * flat_sides_len[i] - 1 + curInd[i]
        ][::-1]

        for y in reversed(range(i)):
            rowToPrint += [flat_circles[y][flat_sides_len[y] - 1 + curInd[y]]]
            curInd[y] += 1

        print(*rowToPrint, sep=" ")


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
