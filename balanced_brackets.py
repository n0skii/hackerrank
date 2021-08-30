#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isBalanced(s):
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    stack: list = list()
    for char in s:
        if char in opening:
            stack.append(char)
        else:
            if len(stack) == 0:
                return "NO"
            lastBracket = stack.pop()
            match = False
            for i in range(3):
                if lastBracket == opening[i] and char == closing[i]:
                    match = True
                    break
            if not match:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + "\n")

    fptr.close()
