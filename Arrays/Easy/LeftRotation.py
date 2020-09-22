#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    a_copy = a.copy()
    for i in range(0,len(a)):
        if i-d >=0:
            new_place = i-d
        elif i-d < 0:
            new_place = len(a) - (d-i)
        a_copy[new_place] = a[i]
    return a_copy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
