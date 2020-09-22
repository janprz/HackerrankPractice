#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    countingArr = [0] * 100
    resultArr = [0] * len(arr)

    for val in arr:
        countingArr[val] += 1
    iterator = 0
    for i in range(0,100):
        for j in range(0,countingArr[i]):
            resultArr[iterator] = i
            iterator += 1
    return resultArr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
