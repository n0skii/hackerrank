#!/bin/python3

from ast import fix_missing_locations
import math
import os
import random
import re
import sys

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#
class Cluster:
    def __init__(self, clusterNum) -> None:
        self.clusterNum = clusterNum
        self.items = 0


def componentsInGraph(gb):
    overallMap = dict()
    clusterMap = dict()
    currentClusterNum = 1
    # Write your code here
    for edge in gb:
        firstIn = edge[0] in overallMap
        secondIn = edge[1] in overallMap
        if not firstIn and not secondIn:
            toAdd = Cluster(currentClusterNum)
            toAdd.items += 2
            overallMap[edge[0]] = currentClusterNum
            overallMap[edge[1]] = currentClusterNum
            clusterMap[currentClusterNum] = toAdd

            currentClusterNum += 1
        elif not firstIn:
            id, toChange = getAndChangeIds(clusterMap[overallMap[edge[1]]])
            for iid in toChange:
                clusterMap[iid] = id
            clusterMap[id].items += 1
            overallMap[edge[0]] = overallMap[edge[1]]
        elif not secondIn:
            id, toChange = getAndChangeIds(clusterMap[overallMap[edge[0]]])
            for iid in toChange:
                clusterMap[iid] = id
            clusterMap[id].items += 1
            overallMap[edge[1]] = overallMap[edge[0]]
        else:
            leftClusterId, toChange = getAndChangeIds(clusterMap[overallMap[edge[0]]])
            for iid in toChange:
                clusterMap[iid] = leftClusterId
            rightClusterId, toChange = getAndChangeIds(clusterMap[overallMap[edge[1]]])
            for iid in toChange:
                clusterMap[iid] = rightClusterId

            if (
                clusterMap[leftClusterId].clusterNum
                != clusterMap[rightClusterId].clusterNum
            ):
                clusterMap[leftClusterId].items += clusterMap[rightClusterId].items
                clusterMap[rightClusterId] = clusterMap[leftClusterId]

    min = float("inf")
    max = float("-inf")
    for value in overallMap.values():
        length = clusterMap[value].items
        if length < min:
            min = length
        if length > max:
            max = length
    return [min, max]


def getAndChangeIds(node: Cluster, clusterMap: dict):
    id = node.clusterNum
    toChange = list()
    while clusterMap[id].clusterNum != id:
        toChange.append(id)
        id = clusterMap[id].clusterNum

    return [id, toChange]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
