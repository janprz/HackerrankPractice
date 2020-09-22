#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    modulo_array = [0]*k
    result = 0
    for val in s:
        remainder = val%k
        modulo_array[remainder] += 1
    result += min(modulo_array[0],1)

    if k % 2 == 0:
        result += min(modulo_array[k//2],1)
    
    for i in range(1,k//2+1):
        if i != k-i:
            result += max(modulo_array[i],modulo_array[k-i])
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
