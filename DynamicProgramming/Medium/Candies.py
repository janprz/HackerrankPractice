#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    arr_len = len(arr)
    candies_arr = [1]*arr_len
    for i in range(1,arr_len):
        if arr[i] > arr[i-1]:
            candies_arr[i] = candies_arr[i-1]+1
    for i in range(arr_len-1,0,-1):
        if arr[i-1] > arr[i] and candies_arr[i-1] <= candies_arr[i]:
            candies_arr[i-1] = candies_arr[i]+1
    return sum(candies_arr) 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
