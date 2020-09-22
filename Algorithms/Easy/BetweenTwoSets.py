#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    elements = 0
    for i in range(1,101):
        isAaFactor = True
        isAFactorOfB = True
        for value in a:
            if i % value != 0:
                isAaFactor = False
                break
        for value in b:
            if value % i:
                isAFactorOfB = False
                break
        if isAaFactor == True and isAFactorOfB == True:
            elements += 1
    return elements

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
