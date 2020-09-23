#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_hourglass_sum = -math.inf
    for i in range(0,len(arr)-2):
        for j in range(0,len(arr)-2):
            temp_hourglass_sum = arr[0+i][0+j]+arr[0+i][1+j]+arr[0+i][2+j]+arr[1+i][1+j]+ arr[2+i][0+j]+arr[2+i][1+j]+arr[2+i][2+j]
            if max_hourglass_sum < temp_hourglass_sum:
                max_hourglass_sum = temp_hourglass_sum
            print(temp_hourglass_sum)
    return max_hourglass_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
