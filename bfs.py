#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#


class Node:
    def __init__(self, posX: int, posY: int, distGain, curDist) -> None:
        self.curDist = curDist + 1
        self.x = posX
        self.y = posY
        self.gain = distGain
        pass


def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    root = Node(startX, startY, 0, 0)
    curNodes = [root]

    visited = list([startX, startY])

    while True:
        bestNode: Node = None
        bestInd = None
        for i, node in enumerate(curNodes):
            node: Node
            if node.x == goalX and node.y == goalY:
                return node.curDist
            if (
                bestNode == None
                or bestNode.gain < node.gain
                or (bestNode.gain == node.gain and bestNode.curDist > node.curDist)
            ):
                bestNode = node
                bestInd = i
        curNodes.pop(bestInd)
        node = bestNode

        newPos = node.x + 1
        if (
            newPos != n
            and grid[node.y][newPos] == "."
            and [newPos, node.y] not in visited
        ):
            distGain = 1 if abs(goalX - node.x) - abs(goalX - newPos) > 0 else -1
            curNodes.append(Node(newPos, node.y, distGain, node.curDist))
            visited.append([newPos, node.y])

        newPos = node.y + 1
        if (
            newPos != n
            and grid[newPos][node.x] == "."
            and [node.x, newPos] not in visited
        ):
            distGain = 1 if abs(goalY - node.y) - abs(goalY - newPos) > 0 else -1
            curNodes.append(Node(node.x, newPos, distGain, node.curDist))
            visited.append([node.x, newPos])

        newPos = node.x - 1
        if (
            newPos != -1
            and grid[node.y][newPos] == "."
            and [newPos, node.y] not in visited
        ):
            distGain = 1 if abs(goalX - node.x) - abs(goalX - newPos) > 0 else -1
            curNodes.append(Node(newPos, node.y, distGain, node.curDist))
            visited.append([newPos, node.y])

        newPos = node.y - 1
        if (
            newPos != -1
            and grid[newPos][node.x] == "."
            and [node.x, newPos] not in visited
        ):
            distGain = 1 if abs(goalY - node.y) - abs(goalY - newPos) > 0 else -1
            curNodes.append(Node(node.x, newPos, distGain, node.curDist))
            visited.append([node.x, newPos])


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + "\n")

    fptr.close()
