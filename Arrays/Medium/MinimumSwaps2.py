#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n_swaps = 0
    i = 0
    while i != len(arr):
        print(i)
        if arr[i]-1 != i:
            n = arr[i]
            arr[i],arr[n-1] = arr[n-1],arr[i]
            i -= 1
            n_swaps += 1
        i += 1
    return n_swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
