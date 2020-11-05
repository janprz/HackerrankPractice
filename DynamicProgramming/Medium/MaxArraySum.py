#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    sum_kad = [0]*len(arr)
    sum_kad[0] = arr[0]
    sum_kad[1] = max([arr[1],arr[0]])
    for i in range(2,len(arr)):
        sum_kad[i] = max([sum_kad[i-2]+arr[i],sum_kad[i-1],arr[i]])
        print(sum_kad[i])
    return sum_kad[-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
