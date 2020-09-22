#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    max_sum = sum(arr[1:5])
    min_sum = sum(arr[0:4])
    print('{} {}'.format(min_sum,max_sum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
