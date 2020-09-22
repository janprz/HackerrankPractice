#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    observed_arr = [0] * 5
    for val in arr:
        observed_arr[val-1] += 1
    max_obs = max(observed_arr)
    for i in range(1,6):
        if observed_arr[i-1] == max_obs:
            return i
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
