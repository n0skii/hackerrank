#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#


class Node(object):
    def __init__(self) -> None:
        super().__init__()
        self.count = 0
        self.childMap = dict()
        self.childNum = 0

    # def isRoot(self):
    #     if self.count == 0:
    #         return True
    #     else:
    #         return False

    # def isLeaf(self):
    #     if self.childNum == 0:
    #         return True
    #     else:
    #         return False


def contacts(queries):
    # Write your code here
    trie = Node()

    for q in queries:
        action, content = q.split(" ")
        if action == "add":
            curNode: Node = trie
            for c in content:
                if c in curNode.childMap:
                    curNode = curNode.childMap[c]
                    curNode.count += 1
                else:
                    toAdd = Node()
                    toAdd.count = 1
                    curNode.childMap[c] = Node()
                    curNode = toAdd
        if action == "find":
            curNode: Node = trie
            for c in content:
                if c in curNode.childMap:
                    curNode = curNode.childMap[c]
                else:
                    return 0
            return curNode.count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
