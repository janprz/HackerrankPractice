#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    n_invs = mergeSort(arr,0,len(arr)-1)
    return n_invs

def mergeSort(arr,l,r):
    if l<r:
        m = l+(r-l)//2
        inv_l = mergeSort(arr,l,m)
        inv_r = mergeSort(arr,m+1,r)
        inv_aux = merge(arr,l,m,r)
        return inv_l+ inv_r + inv_aux
    return 0

def merge(arr,l,m,r):

    n_inv = 0

    left_arr = [0] * (m-l + 1)
    right_arr = [0] * (r-m)

    for i in range(0,m-l+1):
        left_arr[i] = arr[l+i]
    for i in range(0,r-m):
        right_arr[i] = arr[m+1+i]

    i = 0 # left array iterator
    j = 0 # right array iterator
    k = l # merged array iterator

    while i < (m-l + 1) and j < r-m:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
            k += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            k += 1
            n_inv += m-i+1
    
    while i < m-l+1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < r-m:
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    return n_inv



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
