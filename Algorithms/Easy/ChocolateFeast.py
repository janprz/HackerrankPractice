#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    n_choc = 0
    rest_wrappers = -1
    n_choc += n//c
    curr_wrappers = n_choc
    while curr_wrappers >= m:
        rest_wrappers = curr_wrappers%m
        new_wrappers = curr_wrappers//m
        curr_wrappers = new_wrappers + rest_wrappers
        n_choc += new_wrappers
    return n_choc


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
