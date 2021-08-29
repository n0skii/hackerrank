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


def contacts(queries):
    # Write your code here
    pass


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
