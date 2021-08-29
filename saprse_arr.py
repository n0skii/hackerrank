#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Counter

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#


class Node(object):
    def __init__(self) -> None:
        super().__init__()
        self.childMap = dict()
        self.childNum = 0
        self.count = -1


def matchingStrings(strings, queries):
    trie = Node()

    for s in strings:
        curNode: Node = trie
        for char in s:
            if char in curNode.childMap:
                curNode = curNode.childMap[char]
            else:
                newNode = Node()
                newNode.count = 0
                curNode.childMap[char] = newNode
                curNode = newNode
        curNode.count += 1

    for q in queries:
        curNode: Node = trie
        alreadyPrinted = False
        for char in q:
            if char in curNode.childMap:
                curNode = curNode.childMap[char]
            else:
                print("0")
                alreadyPrinted = True
                break
        if not alreadyPrinted:
            print(curNode.count)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write("\n".join(map(str, res)))
    fptr.write("\n")

    fptr.close()
