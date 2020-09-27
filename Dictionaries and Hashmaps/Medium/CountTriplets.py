#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    right = {}
    left = {}
    num_triplets = 0
    for val in arr:
        right[val] = right.get(val,0) + 1
    for val in arr:
        right[val] = max(right[val] - 1,0)
        num_triplets += right.get(val*r,0) * left.get(val/r,0)
        left[val] = left.get(val,0) + 1
    return num_triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
